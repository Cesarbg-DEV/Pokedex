from django.urls import path, include
from . import views
from pokedex.views import pokemon
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home, name='Home'),
    #path('',views.pokemon,name='Pokemon'),
    #path('',pokemon.as_view(),name='Pokemon'),
    path('pkm/<int:id>',views.pkm, name='pkm'),

    path('pokemon/new', views.pokemon_new, name="pokemon New"),
]
