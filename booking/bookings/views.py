from bookings.models import Booking
from bookings.serializers import BookingSerializer
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

    def post(self, request, pk):
        booking = Booking.objects.get(pk=pk)
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
