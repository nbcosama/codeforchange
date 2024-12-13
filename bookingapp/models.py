from django.db import models
from sambandhanewapp.models import *
#Booking System

class Booking(models.Model):
    patientID = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='patient')
    uuID = models.CharField(max_length=100, null=True, default="")
    bookingDate = models.CharField(max_length=100, null=True, default="")
    bookingTime = models.TimeField()
    doctorID = models.CharField(max_length=255)
    payment = models.BooleanField(default=False)
    status = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.patientID.userID
    