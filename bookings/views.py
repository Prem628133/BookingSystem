from bookings.models import Booking, Offer, Service
from django.utils import timezone
from bookings.serializers import BookingSerializer, OfferSerializer, ServiceSerializer, UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from bookings.permissions import IsAdmin
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


class BookingListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):

        booking, created = Booking.objects.get_or_create(
            customer=request.user,
            booking_date=request.data.get("booking_date"),
            booking_time=request.data.get("booking_time"),
            defaults={
                "number_of_guests": request.data.get("number_of_guests"),
            }
        )

        # If already exists → update fields
        if not created:
            booking.number_of_guests = request.data.get("number_of_guests")
            booking.save()

        # Update services
        service_ids = request.data.get("service_ids", [])
        if service_ids:
            booking.services.set(service_ids)

        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=201)


class BookingConfirmAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, id):
        booking = get_object_or_404(Booking, id=id)

        booking.is_confirmed = True
        booking.status = 'Confirmed'
        booking.save()

        return Response(
            {"message": "Booking confirmed successfully"},
            status=status.HTTP_200_OK
        )


class BookingCancelAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, id):
        booking = get_object_or_404(Booking, id=id)

        booking.status = 'Cancelled'
        booking.cancelled_at = timezone.now()

        booking.save()

        return Response(
            {"message": "Booking cancelled successfully"},
            status=status.HTTP_200_OK
        )


class ServiceListCreateAPIView(APIView):
    """List all services or create a new service"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != 'ADMIN':
            return Response({"error": "Only admin can create services"}, status=403)

        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class OfferListCreateAPIView(APIView):
    """List all offers or create a new offer"""

    def get(self, request, *args, **kwargs):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()


class UserCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
