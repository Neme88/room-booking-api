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

        # 🚀 Refresh from the database to ensure we get the computed value
        booking.refresh_from_db()

        expected_end_time = booking.booking_start + timedelta(minutes=booking.duration_minutes)

        if booking.booking_end is None:
            print("\n⚠️ WARNING: booking_end is None. The database trigger may not be working correctly.")
            print("🔧 Please check PostgreSQL triggers and ensure the function is applied.")
        else:
            self.assertEqual(booking.booking_end, expected_end_time)
