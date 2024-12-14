from rest_framework import serializers
from rest_framework.exception import validationError
from Produits.models import Produit
from serializers.Createur import CreateurSerializer


class ProduitSerializers(serializers.ModelSerializer):
    createur = CreateurSerializer

    class Meta:
        model = Produit
        fields = ['createur', 'categorie', 'nom', 'description', 'prix', 'stock', 'image', 'date_ajout']


