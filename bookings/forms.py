# bookings/forms.py
from django import forms
from bookings.models import Booking, Service, Offer, User


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'booking_date', 'booking_time',
                  'number_of_guests', 'status', 'services']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
            'services': forms.CheckboxSelectMultiple(),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'offers',
                  'duration', 'category', 'is_available', 'image_url']
        widgets = {
            'offers': forms.CheckboxSelectMultiple,
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']
