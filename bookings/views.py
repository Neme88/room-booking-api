from rest_framework import viewsets
from .models import RoomBooking
from .serializers import RoomBookingSerializer

class RoomBookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on RoomBooking.
    """
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer

