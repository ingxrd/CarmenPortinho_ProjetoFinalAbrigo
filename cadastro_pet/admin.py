from django.contrib import admin
from cadastro_pet.models import Pet 
# Register your models here.

@admin.register(Pet)
class CadastroAdmin(admin.ModelAdmin):
    #Quais campos irá aparecer no painel administrativo
    list_display = ['nome_pet', 'raca_pet', 'especie_pet', 'imagem']
    search_fields = ['nome_pet', 'raca_pet', 'especie_pet']
    list_filter = ['data_criacao']