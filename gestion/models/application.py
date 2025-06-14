from django.db import models
from .utilisateur import Utilisateur

class Application(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
