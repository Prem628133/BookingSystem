from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bookings.models import User, Booking, Service, Offer


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role", "phone_number")}),
    )


admin.site.register(Booking)
admin.site.register(Service)
admin.site.register(Offer)
