from django.db import models
from charlas.models import Charla
from usuarios.models import SpinqUser


class CategoriaOpinion(models.Model):
    ''' categorias sobre las que se opina () '''
    nombre = models.CharField(max_length=80)
    mas_es_bueno = models.BooleanField(null=True, default=True)
    maximo = models.IntegerField(default=4,
                help_text='Maximo valor de la valoracion posible. '
                            'Si es 1 entonces solo podes elegir pulgar arriba o abajo. '
                            'Si son 5 pueden ser estrellas por ejemplo')
    default_value = models.IntegerField(default=2, help_text='Valor predeterminado al mostrarse a los usuarios')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Opinion(models.Model):
    ''' cada una de las opiniones de los usuarios. Puede ser en el contexto de una charla o algo más general '''
    charla = models.ForeignKey(Charla, null=True, blank=True, on_delete=models.SET_NULL,
                                help_text='Vacío si esta opinando en general del disertante')
    spinq_user = models.ForeignKey(SpinqUser, on_delete=models.CASCADE)
    anonima = models.BooleanField(default=True)
    categoria = models.ForeignKey(CategoriaOpinion, on_delete=models.CASCADE)
    valoracion = models.IntegerField()
    observaciones = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '@{} {}/{} {}'.format(self.spinq_user.nombre, self.valoracion, self.categoria.maximo, self.charla)

    def save(self, *args, **kwargs):
        # ver que los valores no se salgan del rango de su categoria
        if self.valoracion > self.categoria.maximo:
            self.valoracion = self.categoria.maximo
        elif self.valoracion < 0:
            self.valoracion = 0
        super().save(*args, **kwargs)

