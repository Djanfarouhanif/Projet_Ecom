from django.contrib import admin
from .models import Commande

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client','createur','produits', 'status', 'total')

admin.site.register(Commande, CommandeAdmin)