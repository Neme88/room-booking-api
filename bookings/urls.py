from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomBookingViewSet

router = DefaultRouter()
router.register(r'room_bookings', RoomBookingViewSet)  # Auto-generates CRUD URLs

urlpatterns = [
    path('', include(router.urls)),
]
