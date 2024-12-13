from django.urls import path
from . import views

urlpatterns = [
    
    path('postBookings' , views.postBookings, name='postBookings'),
    path('getMyBookings' , views.getMyBookings, name='getMyBookings'),
    path('updateBookings' , views.updateBookings, name='updateBookings'),
    
]




