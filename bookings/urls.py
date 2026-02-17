from django.urls import path
from .views import BookingConfirmAPIView, BookingListCreateAPIView, BookingCancelAPIView, OfferListCreateAPIView, ServiceListCreateAPIView

urlpatterns = [
    path('bookings/', BookingListCreateAPIView.as_view(),
         name='booking-list-create'),
    path('bookings/<int:id>/confirm/', BookingConfirmAPIView.as_view(),
         name='booking-confirm'),
    path('bookings/<int:id>/cancel/', BookingCancelAPIView.as_view(),
         name='booking-cancel'),

    path('offers/', OfferListCreateAPIView.as_view(), name='offer-list-create'),
    path('services/', ServiceListCreateAPIView.as_view(),
         name='service-list-create'),
]
