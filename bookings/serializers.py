from rest_framework import serializers
from bookings.models import Booking, Customer, Service, Offer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class BookingMiniSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'booking_date',
            'booking_time',
            'number_of_guests',
            'status',
            'services'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    bookings = BookingMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'email',
            'phone_number',
            'bookings'
        ]


# Booking Serializer

class BookingSerializer(serializers.ModelSerializer):

    # Display full service details
    services = ServiceSerializer(many=True, read_only=True)

    # Accept only IDs while creating/updating
    service_ids = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Booking
        fields = [
            'id',
            'customer',
            'booking_date',
            'booking_time',
            'number_of_guests',
            'status',
            'services',
            'service_ids'
        ]

    def create(self, validated_data):
        service_ids = validated_data.pop('service_ids', [])
        booking = Booking.objects.create(**validated_data)
        booking.services.set(service_ids)
        return booking

    def update(self, instance, validated_data):
        service_ids = validated_data.pop('service_ids', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if service_ids is not None:
            instance.services.set(service_ids)

        instance.save()
        return instance


# Offer Serializer

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
