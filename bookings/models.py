
import uuid
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

class Booking(models.Model):
    PENDING, CONFIRMED, CANCELLED = "PENDING", "CONFIRMED", "CANCELLED"
    STATUS_CHOICES = [(PENDING, "Pending"), (CONFIRMED, "Confirmed"), (CANCELLED, "Cancelled")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey("rooms.Room", on_delete=models.PROTECT, related_name="bookings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="bookings")
    booking_start = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    booking_end = models.DateTimeField(editable=False, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-booking_start"]
        indexes = [models.Index(fields=["room", "booking_start", "booking_end"])]
        constraints = [
            models.CheckConstraint(check=Q(duration_minutes__gte=0), name="booking_duration_positive"),
        ]

    def _compute_end(self):
        if self.booking_start and self.duration_minutes is not None:
            return self.booking_start + timedelta(minutes=self.duration_minutes)

    def clean(self):
        # basic overlap guard (DB-agnostic)
        end = self._compute_end()
        if end and end <= self.booking_start:
            raise ValueError("booking_end must be after booking_start.")
        if not self.room.is_active:
            raise ValueError("Room is not available for booking.")
        clash_qs = Booking.objects.filter(
            room=self.room,
            status__in=[Booking.PENDING, Booking.CONFIRMED],
            booking_start__lt=end,
            booking_end__gt=self.booking_start,
        )
        if self.pk:
            clash_qs = clash_qs.exclude(pk=self.pk)
        if clash_qs.exists():
            raise ValueError("This room is already booked for the given time range.")

    def save(self, *args, **kwargs):
        if self.booking_start and timezone.is_naive(self.booking_start):
            self.booking_start = timezone.make_aware(self.booking_start, timezone.get_current_timezone())
        self.booking_end = self._compute_end()
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room} / {self.user} @ {self.booking_start}"



