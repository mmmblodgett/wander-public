from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
    privacy = models.CharField(max_length=7, default="public")

class Place(models.Model):
    user = models.ManyToManyField(User, related_name="places")
    label = models.CharField(max_length=128)
    lat = models.DecimalField(max_digits=10, decimal_places=4)
    lng = models.DecimalField(max_digits=10, decimal_places=4)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)