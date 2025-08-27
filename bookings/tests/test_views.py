from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from bookings.models import RoomBooking
from django.utils.timezone import now
import uuid

class RoomBookingAPITest(TestCase):
    def setUp(self):
        """Setup test client and create a test booking"""
        self.client = APIClient()
        self.booking = RoomBooking.objects.create(
            room_id=uuid.uuid4(),
            booked_by="Test User",
            booking_start=now(),
            duration_minutes=60
        )
        self.url = f'/api/room_bookings/{self.booking.room_id}/'

    def test_list_bookings(self):
        """Test retrieving all bookings"""
        response = self.client.get('/api/room_bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_booking(self):
        """Test creating a new booking"""
        data = {
            "booked_by": "Alice",
            "booking_start": "2025-02-15T10:00:00Z",
            "duration_minutes": 120
        }
        response = self.client.post('/api/room_bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('room_id', response.data)

    def test_retrieve_booking(self):
        """Test retrieving a single booking"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['room_id'], str(self.booking.room_id))

    def test_update_booking(self):
        """Test updating a booking"""
        data = {
            "booked_by": "Updated User",
            "booking_start": "2025-02-15T10:00:00Z",
            "duration_minutes": 90
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['booked_by'], "Updated User")

    def test_delete_booking(self):
        """Test deleting a booking"""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_booking_end_is_read_only(self):
        """Test that booking_end is not modifiable via API"""
        data = {
            "booked_by": "Bob",
            "booking_start": "2025-02-15T10:00:00Z",
            "duration_minutes": 60,
            "booking_end": "2025-02-15T12:00:00Z"  # Trying to modify booking_end
        }
        response = self.client.post('/api/room_bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data['booking_end'], "2025-02-15T12:00:00Z")  # Should be computed
