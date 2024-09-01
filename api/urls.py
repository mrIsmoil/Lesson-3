
from django.contrib import admin
from django.urls import include, path

from api.views import CarViewSet

urlpatterns = [
    path('', CarViewSet.as_view({'get':'list'})),
]
