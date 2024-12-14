"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Clients.views import ClientViewset, LoginViewset, LogoutViewset
from Createur.views import CreateurViewset
from Produits.views import Produitviewset
from Commandes.views import CommandeViewset

router = DefaultRouter()
# creation de routre pour le client
router.register(r'user', ClientViewset, basename="signup")

router.register(r'login', LoginViewset, basename="login")
router.register(r'logout', LogoutViewset, basename="logout")
# Creation de route pour le createur

router.register(r'createur', CreateurViewset, basename="createur")

# Creation de route pour la creation de produits
router.register(r'produit', Produitviewset, basename="produit")

# URL pour passer les commandes 
router.register(r'commande', CommandeViewset, basename='commande')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
