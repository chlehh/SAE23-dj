from django.db import models
from .type_serveur import TypeServeur

class Serveur(models.Model):
    nom = models.CharField(max_length=100)
    type_serveur = models.ForeignKey(TypeServeur, on_delete=models.CASCADE)
    nb_processeurs = models.PositiveIntegerField()
    capacite_memoire = models.PositiveIntegerField(help_text="En Mo")
    capacite_stockage = models.PositiveIntegerField(help_text="En Go")

    def __str__(self):
        return self.nom
