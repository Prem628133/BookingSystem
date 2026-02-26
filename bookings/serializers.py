from rest_framework import serializers
from bookings.models import Booking, Service, Offer, User


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


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user
