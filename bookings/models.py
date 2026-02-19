from django.db import models
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        unique_together = [
            ('email', 'phone_number')
        ]


class Booking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="bookings", null=True, blank=True)

    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    services = models.ManyToManyField('Service', blank=True)

    class Meta:
        unique_together = [
            ('customer', 'booking_date', 'booking_time')
        ]

    def __str__(self):
        return f"{self.customer.name} - {self.status}"

    def save(self, *args, **kwargs):
        if self.status == 'Confirmed' and not self.confirmed_at:
            self.confirmed_at = timezone.now()
            self.is_confirmed = True
        super().save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offers = models.ManyToManyField('Offer', blank=True)
    duration = models.DurationField()
    category = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    image_url = models.URLField(blank=True, null=True)


class Offer(models.Model):
    name = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.discount_percentage}%)"
