from django.contrib import admin
from .models import Pokemon, Estadistica, Evolucion, Movimiento

admin.site.register(Pokemon)
admin.site.register(Estadistica)
admin.site.register(Evolucion)
admin.site.register(Movimiento)
