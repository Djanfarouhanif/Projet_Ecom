from django.db import models

from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

