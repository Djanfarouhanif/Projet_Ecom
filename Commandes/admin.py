from django.contrib import admin
from .models import Commande

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('status', 'total')
    
admin.site.register(Commande, CommandeAdmin)