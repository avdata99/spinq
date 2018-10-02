from django.contrib import admin
from .models import CategoriaOpinion, Opinion


@admin.register(CategoriaOpinion)
class LugarAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'default_value', 'maximo', 'mas_es_bueno']
    

@admin.register(Opinion)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['charla', 'spinq_user', 'anonima', 'categoria', 'valoracion']