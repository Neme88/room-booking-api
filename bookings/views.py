from rest_framework import viewsets
from .models import RoomBooking
from .serializers import RoomBookingSerializer

class RoomBookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on RoomBooking.
    """
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer

    def perform_create(self, serializer):
        """ Ensure booking_end is fetched after saving """
        instance = serializer.save()  # Save booking
        instance.refresh_from_db()  # Refresh to get computed booking_end
