from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Createur(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    contact = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username



    