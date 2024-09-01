from django.shortcuts import render
from api.models import Car
from api.serializers import CarSerializer
from rest_framework import routers, serializers, viewsets # type: ignore

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
