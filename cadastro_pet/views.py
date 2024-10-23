import uuid
from django.shortcuts import render #para renderizar html
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse 
from cadastro_pet.forms import PetForm
from cadastro_pet.models import Pet


@csrf_protect
def criar_pet(request):
    #tenho que usar o método POST para criar os pets.
    success = False
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.id = uuid.uuid4()
            pet.save()
            success = True
            form = PetForm()
    else:
        form = PetForm()

    return render (request, 'cadastro_pet.html', {'form': form, 'success':success})


