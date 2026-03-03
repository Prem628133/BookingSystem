from django.urls import path
from . import web_views
from .views import BookingConfirmAPIView, BookingListCreateAPIView, BookingCancelAPIView, OfferListCreateAPIView, ServiceListCreateAPIView, UserCreateAPIView

urlpatterns = [
    # ---- API URLs ----
    path('api/bookings/', BookingListCreateAPIView.as_view(),
         name='api_booking_list_create'),
    path('api/bookings/<int:id>/confirm/', BookingConfirmAPIView.as_view(),
         name='api_booking_confirm'),
    path('api/bookings/<int:id>/cancel/', BookingCancelAPIView.as_view(),
         name='api_booking_cancel'),
    path('api/services/', ServiceListCreateAPIView.as_view(),
         name='api_service_list_create'),
    path('api/offers/', OfferListCreateAPIView.as_view(),
         name='api_offer_list_create'),
    path('api/users/create/', UserCreateAPIView.as_view(),
         name='api_user_create'),

    # ---- Web URLs ----
    path('bookings/', web_views.booking_list, name='booking_list'),
    path('bookings/create/', web_views.booking_create, name='booking_create'),
    path('bookings/<int:pk>/update/', web_views.booking_update,
         name='booking_update'),
    path('bookings/<int:pk>/delete/', web_views.booking_delete,
         name='booking_delete'),
    path('bookings/<int:pk>/confirm/', web_views.booking_confirm,
         name='booking_confirm'),
    path('bookings/<int:pk>/cancel/', web_views.booking_cancel,
         name='booking_cancel'),

    path('services/', web_views.service_list, name='service_list'),
    path('services/create/', web_views.service_create, name='service_create'),

    path('offers/', web_views.offer_list, name='offer_list'),
    path('offers/create/', web_views.offer_create, name='offer_create'),

    path('users/', web_views.user_list, name='user_list'),
    path('users/create/', web_views.user_create, name='user_create'),
    path('test-base/', web_views.test_base_view, name='test_base'),
]
