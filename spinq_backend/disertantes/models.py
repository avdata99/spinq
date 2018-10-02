from django.db import models
from charlas.models import Charla


class Disertante(models.Models):
    nombre = models.CharField(max_length=80)
    bio = models.TextField(null=True, blank=True)
    pic = VersatileImageField(upload_to='users/pics', null=True, blank=True)

    def __str__(self):
        return self.nombre


class DisertanteEnCharla(models.Model):
    disertante = models.ForeignKey(Disertante, on_delete=models.CASCADE)
    charla = models.ForeignKey(Charla, on_delete=models.CASCADE)

    def __str__(self):
        return '{} en {}'.format(self.disertante.nombre, self.charla.nombre)