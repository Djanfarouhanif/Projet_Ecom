from django.contrib import admin
from .models import Categorie

class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']


admin.site.register(Categorie, CategorieAdmin)