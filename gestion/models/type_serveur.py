from django.db import models

class TypeServeur(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.type
