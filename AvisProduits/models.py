from django.db import models

# Create your models here.
from Produits.models import Produit
from Clients.models import Client 

class Avis(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="avis")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    commantaire = models.TextField(blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avis de {self.client.user.username} pour {self.produit.nom}"

