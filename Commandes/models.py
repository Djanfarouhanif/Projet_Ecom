from django.db import models
from Clients.models import Client
from Produits.models import Produit
# Create your models here.

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through="ProduitCommande")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices = [("EN ATTENTE", "En attente"),('VALIDE', 'Validée') , ("ANNULE", "Annule")], default="EN ATTENTE")
    date_command = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande {self.id} - {self.client.user.username}"

class ProduitCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    sous_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produit.nom} x{self.quantite} (Commande {self.commande.id})"