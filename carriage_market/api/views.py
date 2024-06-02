from django.shortcuts import render
from rest_framework import generics
from .serializers import WagonSerializer
from .models import Wagon
# Create your views here.

class WagonsView(generics.ListAPIView):
    queryset = Wagon.objects.all()
    serializer_class = WagonSerializer

