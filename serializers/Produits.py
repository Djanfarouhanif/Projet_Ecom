from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from Produits.models import Produit
from serializers.Createur import CreateurSerializer


class ProduitSerializers(serializers.ModelSerializer):

    class Meta:
        model = Produit
        fields = ['id','categorie', 'nom', 'description', 'prix', 'stock', 'image', 'date_ajout']


