from django.contrib import admin
from django.contrib import admin
from .models import RoomBooking

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ("room_id", "booked_by", "booking_start", "duration_minutes", "booking_end")

