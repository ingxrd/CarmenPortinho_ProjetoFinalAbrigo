from django.contrib import admin
from gestao_adocao.models import Adotante

@admin.register(Adotante)
class CadastroAdotante(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone', 'email', 'idade', 'termo_adocao', 'data_criacao', 'pet']
    search_fields = ['nome', 'cpf', 'email']
    list_filter = ['data_criacao']