
from django.contrib import admin
from django.urls import include, path

from .views import CarCreate, CarDetailView

urlpatterns = [
    path('', CarCreate.as_view()),
    
    path('', CarDetailView.as_view()),
]
