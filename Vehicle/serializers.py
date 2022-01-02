from django.db import models
from django.db.models import fields
from .models import Vehicle, VehicleBooking
from rest_framework import serializers

class AddVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'name',
            'vehicle_type',
            'price',
            'speed',
            'wait_time_charges'
        )

class VehicleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBooking
        fields = (
            'vehicle_name',
            'buyer',
            'latitude_coord',
            'longitude_coord'
        )