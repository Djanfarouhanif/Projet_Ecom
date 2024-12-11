from django.db import models

# Create your models here.
from CategoriesProduits.models import Categorie
from Createur.models import Createur

class Produit(models.Model):
    createur = models.ForeignKey(Createur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="Produits/", blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
