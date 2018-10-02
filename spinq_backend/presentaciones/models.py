from django.db import models


class Presentacion(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Poli(models.Model):
    ''' en los slides la pantalla se parte en partes definidas por polígonos 
        habrá algunos públicos y otros podrán ser dibujados por el dueño 
        de la presentación '''
    
    pass


class Slide(models.Model):
    ''' cada una las páginas de una presentación '''
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)