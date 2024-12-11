from rest_framework import serializers
from AvisProduits.models import Avis

class AvisProduitsSerializer(serializer.ModelSerializer):

    class Meta:
        model = Avis
        fields = '__all__'