from django.urls import path

from .views import (
    AddVehicleView,
    GetAllVehicle,
    BookAVehicleView
)

urlpatterns = [
    path('add/', AddVehicleView.as_view(), name='add_vehicle'),
    path('', GetAllVehicle.as_view(), name='get_all_vehicle'),
    path('booking/', BookAVehicleView.as_view(), name='vehicle_booking'),
]