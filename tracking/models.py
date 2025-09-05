from django.db import models
from django.contrib.auth.models import User

# ✅ Choices for user roles
ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('driver', 'Driver'),
    ('worker', 'Worker'),
)

# 👤 UserProfile model to attach role to each user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# 📍 Location model
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 🗑️ WasteEntry model
class WasteEntry(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_kg = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity_kg} kg at {self.location} by {self.added_by.username}"

    class Meta:
        verbose_name_plural = "Waste Entries"
