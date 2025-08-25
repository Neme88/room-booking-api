from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer
from .permissions import IsAdminOrReadOnly

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]

