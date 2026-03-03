# bookings/web_views.py
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bookings.models import Booking, Service, Offer, User
from .forms import BookingForm, ServiceForm, OfferForm, UserForm

# ---------- Bookings ----------


@login_required
def test_base_view(request):
    return render(request, 'bookings/test_base.html')


@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.user.role != 'ADMIN':
        return redirect('booking_list')
    booking.delete()
    return redirect('booking_list')


@login_required
def booking_confirm(request, pk):
    if request.user.role != 'ADMIN':
        return redirect('booking_list')
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = 'Confirmed'
    booking.is_confirmed = True
    booking.save()
    return redirect('booking_list')


@login_required
def booking_cancel(request, pk):
    if request.user.role != 'ADMIN':
        return redirect('booking_list')
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = 'Cancelled'
    booking.cancelled_at = timezone.now()
    booking.save()
    return redirect('booking_list')

# ---------- Services ----------


@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'bookings/service_list.html', {'services': services})


@login_required
def service_create(request):
    if request.user.role != 'ADMIN':
        return redirect('service_list')
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'bookings/service_form.html', {'form': form})

# ---------- Offers ----------


@login_required
def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'bookings/offer_list.html', {'offers': offers})


@login_required
def offer_create(request):
    if request.user.role != 'ADMIN':
        return redirect('offer_list')
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('offer_list')
    else:
        form = OfferForm()
    return render(request, 'bookings/offer_form.html', {'form': form})

# ---------- Users ----------


@login_required
def user_list(request):
    if request.user.role != 'ADMIN':
        return redirect('booking_list')
    users = User.objects.all()
    return render(request, 'bookings/user_list.html', {'users': users})


@login_required
def user_create(request):
    if request.user.role != 'ADMIN':
        return redirect('booking_list')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'bookings/user_form.html', {'form': form})
