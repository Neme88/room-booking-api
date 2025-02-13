from django.test import TestCase
from bookings.models import RoomBooking
from django.utils.timezone import now
import uuid
from datetime import timedelta

class RoomBookingModelTest(TestCase):
    def test_booking_end_is_auto_computed(self):
        """Test that booking_end is correctly computed by the database trigger"""
        booking = RoomBooking.objects.create(
            room_id=uuid.uuid4(),
            booked_by="Jane Doe",
            booking_start=now(),
            duration_minutes=120
        )
        booking.refresh_from_db()
        expected_end_time = booking.booking_start + timedelta(minutes=booking.duration_minutes)
        self.assertEqual(booking.booking_end, expected_end_time)

    def test_duration_must_be_positive(self):
        """Test that duration_minutes must be a positive integer"""
        with self.assertRaises(Exception):
            RoomBooking.objects.create(
                room_id=uuid.uuid4(),
                booked_by="John Doe",
                booking_start=now(),
                duration_minutes=-30
            )

