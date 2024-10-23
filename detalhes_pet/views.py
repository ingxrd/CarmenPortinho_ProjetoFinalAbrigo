from django.shortcuts import render, get_object_or_404
from cadastro_pet.models import Pet

def detalhes_pet(request, id):
    # Busca o pet pelo ID ou retorna 404 se não encontrado
    pet = get_object_or_404(Pet, id=id)
    
    # Template vai mudar conforme o pet 
    return render(request, 'detalhes_pet.html', {'pet': pet})
