from django.shortcuts import render
from cadastro_pet.models import Pet

def home(request):
    pets = Pet.objects.filter(adotado=False)  # Faz filtragem por entre os Pets não adotados
    return render(request, 'home.html', {'pets': pets})
