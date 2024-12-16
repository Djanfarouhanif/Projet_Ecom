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
    # queryset = Commande.objects.all()
    serializer_class = CommandeSerializers
    permission_classes = [IsAuthenticated]
    
    
    # Ajouter un nouveau produits

    # Crée un produit

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
                # Recuper le createur via le produit ajouter
                data_valide = serializer.validated_data.get('produits')
                print(data_valide.createur.user, "data===================")
                user = data_valide.createur.user
                createur = Createur.objects.get(user=user)
                print(createur)
                

                # Récuperé le client
                if Client.objects.filter(user=current_user):
                    current_client = Client.objects.get(user=current_user)

                    commande = Commande.objects.create( client=current_client,createur=createur,**serializer.validated_data)
                # Après l'enregistrement recuper le createur via produit qui est enregistre dans commande
                
                    commande.save()
                    return Response({"success": "Commande crée"}, status=status.HTTP_200_OK)
                # Si le client n'exits pas envoyer un message 204
                return Response({"error": "no client account"}, status=status.HTTP_204_NO_CONTENT)

                
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

    def get_queryset(self):
        # Cette méthode est utilisée pour personnaliser la queryset retournée Filtre les commandes de l'utilisateur authentifié

        # Affichier toute les produits comander associer au createur de produits
        if Createur.objects.filter(user=self.request.user).exists():
            current_createur = Createur.objects.get(user=self.request.user)
            # Facile maintenant parceque chaque commande es associer la commande

            return Commande.objects.filter(createur=current_createur)

        # Afficher toutes les commandes associer au clients
        if Client.objects.filter(user=self.request.user).exists():
            # Récupere le client actuel qui a passer les commande
            current_client = Client.objects.get(user=self.request.user)
            return Commande.objects.filter(client=current_client)


    def list(self, request, *args, **kwargs):
       
       # Cette méthode gère la liste des commandes filtrées par utilisateur 

       # Utiliser la méthode get_querysert() pour obtenir la queryset filtrée

       queryset = self.get_queryset()
       if not queryset:
            return Response([], status=status.HTTP_204_NO_CONTENT) # Retourner une réponse vide avec code 204

       # Sérializer la queryset des commandes 
       serializer = self.get_serializer(queryset, many=True)

       # Retourne la résponse avec les données serialisée

       return Response(serializer.data)
    # Autiriser uniquement pour le moment le client seule a suprimer la commande
    def destroy(self, request, *args, **kwargs):
        # Récuper l'object a suprimer 
        commande = self.get_object()

        current_user = self.request.user

        # Pour ne pas permetre a un createur de suprimer un commande
        if Createur.objects.filter(user=current_user):
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        if Client.objects.filter(user=current_user).exists():
            current_client = Client.objects.get(user=current_user)
            if commande.client == current_client:
                commande.delete()

                return Response({"success": "commende suprimer"}, status=status.HTTP_200_OK)

            

        return Response(status=status.HTTP_403_FORBIDDEN)


        
        


