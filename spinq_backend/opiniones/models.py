from django.db import models
from charlas.models import Charla
from usuarios.models import SpinqUser


class CategoriaOpinion(models.Model):
    ''' categorias sobre las que se opina () '''
    nombre = models.CharField(max_length=80)
    mas_es_bueno = models.BooleanField(null=True, default=True)
    maximo = models.IntegerField(default=5,
                help_text='Maximo valor de la valoracion posible. '
                            'Si es 1 entonces solo podes elegir pulgar arriba o abajo. '
                            'Si son 5 pueden ser estrellas por ejemplo')

    def __str__(self):
        return self.nombre


class Opinion(models.Model):
    charla = models.ForeignKey(Charla, on_delete=models.CASCADE)
    spinq_user = models.ForeignKey(SpinqUser, on_delete=models.CASCADE)
    anonima = models.BooleanField(default=True)


