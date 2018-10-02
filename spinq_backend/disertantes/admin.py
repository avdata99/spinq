from django.contrib import admin
from .models import Disertante, DisertanteEnCharla


@admin.register(Disertante)
class DisertanteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'bio']
    

@admin.register(DisertanteEnCharla)
class DisertanteEnCharlaAdmin(admin.ModelAdmin):
    list_display = ['disertante', 'charla']

