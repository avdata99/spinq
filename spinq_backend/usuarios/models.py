from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from versatileimagefield.fields import VersatileImageField


class SpinqUser(models.Model):
    ''' voy a tener mi propio usuario porque el username de django permite caracteres extraños '''
    nombre = models.CharField(max_length=40)
    bio = models.TextField(null=True, blank=True)
    pic = VersatileImageField(upload_to='users/pics', null=True, blank=True)

    puntos = models.IntegerField(default=0, help_text='Puntaje del usuario')

    def validate_nombre(self):
        ''' validar el nombre de usuario en la plataorma '''
        # pedir un mínimo de largo (los cortos serían pagos)
        # solo permitir guiones bajos
        pass
    
