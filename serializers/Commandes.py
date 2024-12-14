from rest_framework import serializers
from Commandes.models import Commande
from Produits.models import Produit



class CommandeSerializers(serializers.ModelSerializer):

    class Meta: 
        model = Commande
        fields = ['produits', 'total', 'status']