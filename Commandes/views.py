from django.shortcuts import render
from rest_framework import  status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from serializers.Commandes import CommandeSerializers
from .models import Commande


class CommandeViewset(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializers

    
