from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response 
from .models import Createur
from serializers.Createur import CreateurSerializer


class CreateurViewset(viewsets.ModelViewSet):
    queryset = Createur.objects.all()
    serializer_class = CreateurSerializer
