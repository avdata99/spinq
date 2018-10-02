from django.db import models
from django.contrib.auth.models import User


class SpiqUser(models.Model):
    ''' voy a tener mi propio usuario porque el username de django permite caracteres extraños '''
    
    
