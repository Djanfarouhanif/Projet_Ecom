from django.shortcuts import render
from rest_framework import  status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from serializers.Commandes import CommandeSerializers
from .models import Commande
from Createur.models import Createur
from Clients.models import Client
from Produits.models import Produit


class CommandeViewset(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializers
    permission_classes = [IsAuthenticated]
    
    
    # Ajouter un nouveau produits

    # Crée un produit

    def create(self, request, *args, **kwargs):
        print("***********", self.get_serializer())
        current_user = self.request.user
        # serilizer les donnéé récupérer
        serializer = CommandeSerializers(data=request.data)
        if serializer is None:
        # if Createur.objects.filter(user=current_user).exists() :
            pass
            return Response({"error": "Creator is not permissions commande product"}, status=status.HTTP_403_FORBIDDEN)

        else:

            if serializer.is_valid():
                # Récuperé le client
                current_client = Client.objects.get(user=current_user)

                commande = Commande.objects.create(client=current_client, **serializer.validated_data)
                commande.save()

                return Response({"success": "Commande crée"}, status=status.HTTP_200_OK)
            return Response({"error": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
    # Fonction pour listé les produit commander

    def destroy(self, request, *agrs, **kwargs):
        current_user = request.user
        if Client.objects.filter(user=user).exists():
            current_client = Client.objects.get(user=user)
            produit = Commande.objects.filter(client= current_client)
            produit.delete

            return Response({'succes': 'Commande delete'}, status=status.HTTP_200_OK)

        return Response({"error": "Client hane not permission"}, status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        # Ajouter une logique personnalizer 
        queryset = self.filter_queryset(self.get_queryset())
        print('---------------------------------------')
        print(queryset)

        # Customiser les affichicchage
        produit = Produit.objects.all()

        
        
        
        return Response( {'success':serialiers}, status=status.HTTP_200_OK)
            
        
        


