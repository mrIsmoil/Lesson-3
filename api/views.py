from urllib import response
from django.shortcuts import render
from api.models import Car
from api.serializers import CarSerializer
from rest_framework.permissions import AllowAny
from rest_framework import routers, serializers, viewsets # type: ignore
from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.mixins import RetrieveModelMixin

class CarCreate(ListCreateAPIView):

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [AllowAny]

# class CarRetrieve(RetrieveAPIView):
#     def get(self, request):
#         cars = Car.objects.all()  # QuerySet
#         serializer = CarSerializer(cars, many=True)
#         return response(serializer.data)

# class CarUpdateItem(UpdateAPIView):

#     serializer_class = CarSerializer
#     queryset = Car.objects.all()

class CarDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)