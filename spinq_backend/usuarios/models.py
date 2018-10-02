from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from versatileimagefield.fields import VersatileImageField
from django.core.validators import RegexValidator


spinq_nombre_validator = RegexValidator(
                            regex='[a-z_]+',
                            message='Ingresa un nombre válido. Solo letras en minúscula y guiones bajos',
                            code='inválido',
)

class SpinqUser(models.Model):
    ''' voy a tener mi propio usuario porque el username de django permite caracteres extraños '''
    nombre = models.CharField(max_length=40, unique=True, validators=[spinq_nombre_validator])
    bio = models.TextField(null=True, blank=True)
    pic = VersatileImageField(upload_to='users/pics', null=True, blank=True)

    puntos = models.IntegerField(default=0, help_text='Puntaje del usuario (se le da por opinar)')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    
