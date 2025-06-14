from django.db import models
from .serveur import Serveur

class Service(models.Model):
    nom = models.CharField(max_length=100)
    date_lancement = models.DateField()
    espace_memoire_utilise = models.PositiveIntegerField(help_text="En Mo")
    memoire_vive_necessaire = models.PositiveIntegerField(help_text="En Mo")
    serveur = models.ForeignKey(Serveur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
