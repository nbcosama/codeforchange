
from rest_framework import serializers
from .models import *




class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'patientID', 'uuID', 'bookingDate', 'bookingTime', 'doctorID', 'payment', 'status', 'createdAt', 'updatedAt']


