from django.urls import path
from . import views
from pokedex.views import pokemon


urlpatterns = [
    path('',views.home, name='Home'),
    #path('',views.pokemon,name='Pokemon'),
    #path('',pokemon.as_view(),name='Pokemon'),
]