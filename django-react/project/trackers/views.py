from django.shortcuts import render

# Create your views here.
from .models import Worker
from .serializers import WorkerSerializer
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer