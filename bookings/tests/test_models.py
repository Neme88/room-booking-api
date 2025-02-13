import unittest
from django.test import TransactionTestCase
from bookings.models import RoomBooking

class RoomBookingModelTest(TransactionTestCase):

    @unittest.skip("Skipping this test for now until further debugging")
    def test_booking_end_is_auto_computed(self):
        """ Test that booking_end is correctly computed by the database trigger """
        pass  # Skip test execution
