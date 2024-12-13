from django.urls import path
from . import views

urlpatterns = [
    path('meroSathi' , views.meroSathi, name='meroSathi')
]