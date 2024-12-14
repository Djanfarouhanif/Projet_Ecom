from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from rest_framework.response  import Response
from .models import Createur
from serializers.Produits import ProduitSerializers
from .models import Produit


class ProduitSerializer(viewsets.ModelViewSet):
    queryset = Produit
    permission_classe = [AllowAny]
    
