from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *


# Create your views here.

@api_view(['POST'])
def meroSathi(request):
    return Response({"success": True, "message": "Hello World"})