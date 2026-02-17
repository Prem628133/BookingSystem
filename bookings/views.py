from bookings.models import Booking, Offer, Service
from django.utils import timezone
from bookings.serializers import BookingSerializer, OfferSerializer, ServiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BookingListCreateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingConfirmAPIView(APIView):

    def post(self, request, id):
        booking = Booking.objects.get(id=id)
        if not booking:
            return Response(
                {"error": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        booking.is_confirmed = True
        booking.status = 'Confirmed'
        booking.save()

        return Response(
            {"message": "Booking confirmed successfully"},
            status=status.HTTP_200_OK
        )


class BookingCancelAPIView(APIView):

    def post(self, request, id):
        booking = Booking.objects.get(id=id)
        if not booking:
            return Response(
                {"error": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        booking.status = 'Cancelled'
        booking.cancelled_at = timezone.now()

        booking.save()

        return Response(
            {"message": "Booking cancelled successfully"},
            status=status.HTTP_200_OK
        )


class ServiceListCreateAPIView(APIView):
    """List all services or create a new service"""

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
