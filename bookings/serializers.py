from rest_framework import serializers
from .models import Booking, Service, Offer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)  # display
    service_ids = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Booking
        fields = ['id', 'customer_name', 'email', 'phone_number', 'booking_date',
                  'booking_time', 'number_of_guests', 'status', 'services', 'service_ids']

    def update(self, instance, validated_data):
        service_ids = validated_data.pop('service_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Only allow service selection if booking is confirmed
        if instance.status == 'Confirmed' and service_ids is not None:
            instance.services.set(service_ids)

        instance.save()
        return instance


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
