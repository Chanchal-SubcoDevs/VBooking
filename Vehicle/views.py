from django.http import response
from django.shortcuts import render
from rest_framework import  serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    AddVehicleSerializer,
    VehicleBookingSerializer
)
from .models import Vehicle
# Create your views here.

class AddVehicleView(APIView):
    serializer_class = AddVehicleSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode':status_code,
                'message':'A new vehicle added!',
                'data':serializer.data
            }

            return Response(response, status=status_code)


class GetAllVehicle(APIView):
    serializer_class = AddVehicleSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = self.serializer_class(vehicles, many=True)
        response = {
            'success':True,
            'status_code':status.HTTP_200_OK,
            'data':serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)


class BookAVehicleView(APIView):
    serializer_class = VehicleBookingSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode':status_code,
                'message':'A new vehicle added!',
                'data':serializer.data
            }

            return Response(response, status=status_code)