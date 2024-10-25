from django.shortcuts import render, get_object_or_404
from .models import Pet # Importa o modelo Animal

def detalhes_pet(request, id):
    pet = get_object_or_404(Pet, pk=id) # Busca o animal no banco de dados
    context = {
        'pet': pet
    }
    return render(request, 'detalhes_pet/detalhes_pet.html', context)