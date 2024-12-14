from rest_framework import serializers
from Commandes.models import Commande
from Produits.models import Produit


# serialeir le produit pour ajoute dans commande 
class OneProduit(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class CommandeSerializers(serializers.ModelSerializer):

    produits  = OneProduit()

    class Meta: 
        model = Commande
        fields = ['produits', 'total', 'status']