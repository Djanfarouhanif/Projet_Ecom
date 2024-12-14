from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response  import Response
from .models import Createur
from serializers.Produits import ProduitSerializers
from .models import Produit
from django.contrib.auth.models import User


class Produitviewset(viewsets.ModelViewSet):
    
    permission_classe = [IsAuthenticated]
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializers


    def create(self, request):
        # Récuper l'utilisateur en cours

        user = request.user
       
        # Récuper les donnée sérializer
        serializer = ProduitSerializers(data=request.data)
        print(serializer, "*************")
        # Vérifier si l'utisateur courant fait partir des createurs des produits
        if serializer.is_valid():
            if Createur.objects.filter(user= user).exists():
                createur = Createur.objects.get(user=user)
                # Crée un nouveau produit
                
                new_produit = Produit.objects.create(createur=createur, **serializer.validated_data)
                new_produit.save()

                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "user Not matching"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request,*args, **kwargs):
        # Récupérer l'utisateur authentifié
        user = request.user
        print("************")
        print(user)

        # Récupere l'object produit à mettre à jour
        produit = self.get_object() # Cela récupère l'object produit basé sur le pk dans l'url

        # Vérifier si l'utisateur est un créateur
        if Createur.objects.filter(user=user).exists():
            createur = Createur.objects.get(user=user)

            # Vérifier si le produit appartient au créateur

            if produit.createur == createur:
                # Sérialiser les nouvelles données
                serializer = self.get_serializer(produit, data=request.data, partial=True)
                if serializer.is_valid():
                    # Mettre à jour le produit avec les nouvelles donnéds
                    serializer.save()
                    return Response({'status': 'success ', 'produit': serializer.data}, status=status.HTTP_200_OK)
                else:
                    # Si les données du sériaseur ne sont pas valides
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "You are not the creator of this product"}, status=status.HTTP_403_FORBIDDEN)

        else:
            # si l'utisateur ne fait pas partie des createur ou n'est pas enregistre
            return Response({"error": "User not creators"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):

        # Récuper l'object produit a suprimer 
        produit = self.get_object()

        # Vérifier si l'utisateur courent est un createur

        if Createur.objects.filter(user=request.user).exists():
            # Récuper l'utilisateur
            createur = Createur.objects.get(user=request.user)

            # Verifier si le produit appartient cet createur

            if produit.createur == createur:
                # suprimer le produit
                produit.delete()

                return Response({"success": "product delete"}, status=status.HTTP_200_OK)
                
            else:
                return Response({"error": "This product is not matching for createur"}, status=status.HTTP_403_FORBIDDEN)

        else:
            return Response({"error": "User not in createur"}, status=status.HTTP_403_FORBIDDEN)
