from django.contrib.gis.db import models


class Lugar(models.Model):
    nombre = models.CharField(max_length=80)
    punto = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    lugar = models.ForeignKey(Lugar, null=True, blank=True)
    url_mas_info = models.URLField(null=True, blank=True)


class Charla(models.Model):
    nombre = models.CharField(max_length=80)
    lugar = models.ForeignKey(Lugar, null=True, blank=True, help_text='Puede ser un lugar interno dentro del lugar del evento si lo ubiera')

    dia = models.DateField(default=timezone.now)
    hora_desde_instalacion_solicitada = models.TimeField(null=True, blank=True, help_text='Desde que hora se puede entregar el pedido')
    
    def __str__(self):
        return self.nombre
