from django.contrib import admin
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ("id", "room", "user", "booking_start", "booking_end", "duration_minutes", "status", "created_at",)
    list_filter = ("status", "room")
    search_fields = ("room_name", "user_name", "user_email")
    ordering = ("-booking_start",)
    readonly_fields = ("booking_end", "created_at")
