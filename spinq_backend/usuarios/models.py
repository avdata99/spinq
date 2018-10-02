from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


class SpiqUser(models.Model):
    ''' voy a tener mi propio usuario porque el username de django permite caracteres extraños '''
    nombre = models.CharField(max_length=30)
    bio = models.TextField(null=True, blank=True)
    

    def validate_nombre(self):
        ''' validar el nombre de usuario en la plataorma '''
        # pedir un mínimo de largo (los cortos serían pagos)
        # solo permitir guiones bajos
        pass
    
