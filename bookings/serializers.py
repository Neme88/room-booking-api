# bookings/serializers.py
from dateutil import parser
from django.utils import timezone
from rest_framework import serializers
from .models import Booking
from rooms.models import Room

class AnyDateTimeField(serializers.DateTimeField):
    def to_internal_value(self, value):
        if isinstance(value, str):
            try:
                dt = parser.parse(value)
            except Exception:
                self.fail("invalid", format="flexible-date")
            # If only a date supplied, set a default hour
            if len(value.strip()) <= 10:
                dt = dt.replace(hour=9, minute=0, second=0, microsecond=0)
            if timezone.is_naive(dt):
                dt = timezone.make_aware(dt, timezone.get_current_timezone())
            return dt
        return super().to_internal_value(value)

class BookingSerializer(serializers.ModelSerializer):
    booking_start = AnyDateTimeField()
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.filter(is_active=True))
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source="user.id")  # set from request

    class Meta:
        model = Booking
        fields = ["id", "room", "user", "booking_start", "duration_minutes", "booking_end", "status", "created_at"]
        read_only_fields = ["booking_end", "created_at"]
