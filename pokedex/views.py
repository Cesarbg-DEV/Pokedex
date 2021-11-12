from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon , Estadistica
from .forms import Pokemon_form
def home(request):
    return render(request, 'index.html')

def pokemon(request, *args, **kwargs):
    pokemon = Pokemon.objects.all()
    response = {'pokemones': pokemon}
    return render(request,'index.html', response)
def pkm(request,id):
    pkm = Pokemon.objects.get(id=id)
    return render(request,'pkm.html',{'pkm':pkm})

# F O R M #
def pokemon_new(request):

    if request.method == "POST":
        form = Pokemon_form(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.save()
            return redirect('Home')
    else:
        form = Pokemon_form()
        return render(request, "newpkm.html", {'form':form})