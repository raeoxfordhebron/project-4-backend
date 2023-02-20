from django.shortcuts import render
from .models import Job
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import JobSerializer

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permissions_classes = [permissions.AllowAny]
    
# class LanguageViewSet(viewsets.ModelViewSet):
#     queryset = Language.objects.all()
#     serializer_class = LanguageSerializer
#     permissions_classes = [permissions.AllowAny]