from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.allTemp, name='temp'),
    path('temp/new/', views.insertTemp, name='temp-new')
]
