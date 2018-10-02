from django.contrib import admin
from .models import Lugar, Evento, Charla


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'lugar']


@admin.register(Charla)
class CharlaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'evento']
