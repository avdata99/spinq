from usuarios.models import SpinqUser
from django.contrib.gis.db import models


class Presentacion(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(SpinqUser, on_delete=models.SET_NULL, null=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    

class PoliForm(models.Model):
    ''' en los slides la pantalla se parte en partes definidas por polígonos 
        habrá algunos públicos y otros podrán ser creados por el dueño 
        de la presentación '''
    
    creator = models.ForeignKey(SpinqUser, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(null=True, blank=True)

    contenedor = models.PolygonField()


class PoliPart(models.Model):
    ''' cada uno de los polígonos que componene un formulario poli '''
    creator = models.ForeignKey(SpinqUser, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=45)
    poligono = models.PolygonField()


class UsablePoliForm(models.Model):
    ''' un formulario listo para usar en un slide '''
    poliform = models.ForeignKey(PoliForm, on_delete=models.CASCADE)
    bg_color = models.CharField(max_lengt=8, default='FFFFFF80', help_text='RBG + Alpha')
    border_width = models.PositiveIntegerField(default=1)


class UsablePoliPart(models.Model):
    ''' un formulario listo para usar en un slide '''
    polipart = models.ForeignKey(PoliPart, on_delete=models.CASCADE)
    bg_color = models.CharField(max_lengt=8, default='FFFFFF80', help_text='RBG + Alpha')
    border_width = models.PositiveIntegerField(default=1)


class Slide(models.Model):
    ''' cada una las páginas de una presentación '''
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(null=True, blank=True)

