from django.contrib.gis.db import models
from django.utils import timezone


class Lugar(models.Model):
    nombre = models.CharField(max_length=80)
    punto = models.PointField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    lugar = models.ForeignKey(Lugar, null=True, blank=True, on_delete=models.SET_NULL)
    url_mas_info = models.URLField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Charla(models.Model):
    nombre = models.CharField(max_length=80)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)
    lugar = models.ForeignKey(Lugar, null=True, blank=True,
                                help_text='Puede ser un lugar interno dentro del lugar del evento si lo ubiera',
                                on_delete=models.SET_NULL)

    dia = models.DateField(default=timezone.now, null=True)
    hora_inicio = models.TimeField(null=True, blank=True, help_text='Hora de inicio')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
