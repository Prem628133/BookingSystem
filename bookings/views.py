from bookings.models import Booking, Customer, Offer, Service
from django.utils import timezone
from bookings.serializers import BookingSerializer, OfferSerializer, ServiceSerializer, CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateCustomerAPIView(APIView):

    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        customer, created = Customer.objects.update_or_create(
            email=request_data.get('email'),
            phone_number=request_data.get('phone_number'),
        )
        serializer = CustomerSerializer(customer)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(serializer.data, status=status_code)


class BookingListCreateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        service_ids = data.pop("service_ids", [])

        booking, created = Booking.objects.update_or_create(
            customer_id=data.get("customer"),
            booking_date=data.get("booking_date"),
            booking_time=data.get("booking_time"),
            number_of_guests=data.get("number_of_guests"),
        )

        # Update ManyToMany services
        if service_ids:
            booking.services.set(service_ids)

        serializer = BookingSerializer(booking)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )


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
