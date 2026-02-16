from django.urls import path
from .views import BookingConfirmAPIView, BookingListCreateAPIView

urlpatterns = [
    path('bookings/', BookingListCreateAPIView.as_view(),
         name='booking-list-create'),
    path('bookings/<int:pk>/confirm/', BookingConfirmAPIView.as_view(),
         name='booking-confirm'),
]
