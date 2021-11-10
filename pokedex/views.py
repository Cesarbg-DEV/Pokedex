from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon , Estadistica

def home(request):
    return render(request, 'index.html')

def pokemon(request, *args, **kwargs):
    pokemon = Pokemon.objects.all()
    response = {'pokemones': pokemon}
    return render(request,'index.html', response)
def pkm(request,id):
    pkm = Pokemon.objects.get(id=id)
    return render(request,'pkm.html',{'pkm':pkm})