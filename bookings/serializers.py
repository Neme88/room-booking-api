from rest_framework import serializers
from .models import RoomBooking

class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = '__all__'
        read_only_fields = ('booking_end',)  # `booking_end` is computed in DB, so it's read-only
