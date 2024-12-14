from django.contrib import admin
from .models import Produit


class ProduitAdmin(admin.ModelAdmin):
    list_display = ['id','createur', 'categorie', 'nom', 'description', 'prix', 'stock', 'image', 'date_ajout']

admin.site.register(Produit, ProduitAdmin)
