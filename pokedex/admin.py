from django.contrib import admin
from .models import Pokemon
from .models import Estadistica
from .models import Evolucion
from .models import Movimiento

admin.site.register(Pokemon)
admin.site.register(Estadistica)
admin.site.register(Evolucion)
admin.site.register(Movimiento)
