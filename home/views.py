from django.shortcuts import render,redirect
from cadastro_pet.models import Pet
from django.db.models import Q


def home(request):
    pets = Pet.objects.filter(adotado=False)  # Faz filtragem por entre os Pets não adotados
    return render(request, 'home.html', {'pets': pets})


def adote_pet(request):
    #pesquisa e exibição de todos os bichinhos que estão disponiveis para adoçao
    pesquisa_query = request.GET.get('pesquisa_query', None)

    if pesquisa_query:
        # Pesquisa por nome ou raça e animais não adotados
        query_clean = Q(Q(nome_pet__icontains=pesquisa_query) | Q(raca_pet__icontains=pesquisa_query))
        animais = Pet.objects.filter(query_clean, adotado=False)
    else:
        # Se não houver pesquisa, exibe todos os animais não adotados
        animais = Pet.objects.filter(adotado=False)

    return render(request, 'adote.html', {'pesquisa_query': pesquisa_query, 'animais': animais})

#barra de pesquisa
def pesquisar_animais(request):
    if 'pesquisa_query' in request.GET:
        pesquisa_query = request.GET['pesquisa_query']

        #fazendo pesquisa com multiplas palavra chaves e campos
        query_clean = Q(Q(nome_pet__icontains = pesquisa_query) | Q(raca_pet__icontains = pesquisa_query))

        animais = Pet.objects.filter(query_clean, adotado=False)

        #fazendo pesquisa só de um campo
        # animais = CadastroAnimal.objects.filter(nome__icontains = pesquisa_query)
        
        return redirect(request, 'adote.html', {'pesquisa_query':pesquisa_query , 'animais': animais})
    
    else:
        return render(request, 'adote.html', {})

def sobre(request):
    return render(request, 'sobre.html')