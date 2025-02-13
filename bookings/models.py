import uuid
from datetime import timedelta
from django.db import models
class RoomBooking(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booked_by = models.CharField(max_length=255)
    booking_start = models.DateTimeField()
    duration_minutes = models.IntegerField()
    
    # Ensure booking_end is read-only in Django (computed in PostgreSQL)
    booking_end = models.DateTimeField(editable=False, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(duration_minutes__gte=0),
                name="booking_duration_positive"
            )
        ]

    def __str__(self):
        return f"Booking by {self.booked_by} on {self.booking_start}"


