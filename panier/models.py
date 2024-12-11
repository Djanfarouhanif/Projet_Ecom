from django.db import models
from Produits.models import Produit
from Clients.models import Client
# Create your models here.

class Panier(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through="ProduitPanier")

    def __str__(self):
        return f'Panier de {self.client.user.username}'

class ProduitPanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produit.nom} x{self.quantite} (Panier de {self.panier.client.user.username})"

