from django.contrib import admin
from .models import Createur

class CreateurAdmin(admin.ModelAdmin):
    list_display = ['user', 'contact']


admin.site.register(Createur, CreateurAdmin)
