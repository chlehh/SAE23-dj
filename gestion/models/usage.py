from django.db import models
from .application import Application


class Usage(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.application} utilise {self.service}"
