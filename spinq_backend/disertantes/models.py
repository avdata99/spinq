from django.db import models
from charlas.models import Charla
from versatileimagefield.fields import VersatileImageField
from usuarios.models import SpinqUser


class Disertante(models.Model):
    nombre = models.CharField(max_length=80)
    bio = models.TextField(null=True, blank=True)
    pic = VersatileImageField(upload_to='users/pics', null=True, blank=True)
    spinq_user_admin = models.ForeignKey(SpinqUser, null=True,
                                            blank=True,
                                            on_delete=models.SET_NULL,
                                            help_text='Usuario que administra el perfil')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class DisertanteEnCharla(models.Model):
    disertante = models.ForeignKey(Disertante, on_delete=models.CASCADE)
    charla = models.ForeignKey(Charla, on_delete=models.CASCADE)
    spinq_user_added = models.ForeignKey(SpinqUser, null=True,
                                            blank=True,
                                            on_delete=models.SET_NULL,
                                            help_text='Usuario que lo cargo')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} en {}'.format(self.disertante.nombre, self.charla.nombre)