from django.shortcuts import render
from rest_framework import  status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from serializers.Commandes import CommandeSerializers
from .models import Commande
from Createur.models import Createur
from Clients.models import Client


class CommandeViewset(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializers
    permission_classes = [IsAuthenticated]

    # Ajouter un nouveau produits

    def create(self, request, *args, **kwargs):

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
            
            
        
        


