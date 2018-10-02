from django.contrib import admin
from .models import SpinqUser


@admin.register(SpinqUser)
class SpinqUserAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'bio', 'puntos']
    

