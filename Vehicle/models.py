import uuid
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from Auth.models import User

# Create your models here.
class Vehicle(models.Model):
    
    TYPE=[
        ('CAR','car'),
        ('BIKE','bike'),
        ('BYCYCLE','bycycle'),
        ('AUTO','auto'),
        ('TRUCK','truck'),
    ]

    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Vehicle identity')
    name = models.CharField(max_length=255)
    vehicle_type = models.CharField(choices=TYPE, max_length=15, default='CAR')
    price = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    wait_time_charges = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.vehicle_type})"

class VehicleBooking(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Vehicle booking identity')
    vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude_coord = models.FloatField(max_length=20, blank=True, null=True)
    longitude_coord = models.FloatField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.vehicle_name
