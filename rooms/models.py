import uuid
from django.db import models

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True)
    capacity = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)  # admin can disable room
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

