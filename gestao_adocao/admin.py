from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from gestao_adocao.models import Adotante, Pet

@admin.register(Adotante)
class CadastroAdotante(admin.ModelAdmin):
    list_display = ['nome', 
                    'telefone', 
                    'email', 
                    'pet_link',  
                    'status_adocao',
                    'data_criacao', 
                    'exibir_short_descrip_termo', 
                    'exibir_short_descrip_idade',]
    search_fields = ['nome', 'cpf', 'email']
    list_filter = [ 'data_criacao']
    ordering = ['-data_criacao']
    actions = ['aprovar_adocao', 'desaprovar_adocao']  


    # Coluna para exibir o nome do pet com link
    def pet_link(self, obj):
        #informando o nome do nosso app com os argumentos pet.id
        url = reverse("admin:cadastro_pet_pet_change", args=[obj.pet.id])  
        return format_html('<a href="{}">{}</a>', url, obj.pet.nome_pet)

    pet_link.short_description = 'Pet'

    #diminuindo a verbose_name do models
    def exibir_short_descrip_idade(self, obj):
        return obj.idade 
        
    exibir_short_descrip_idade.boolean = True
    exibir_short_descrip_idade.short_description = 'Maior 18 anos'

    def exibir_short_descrip_termo(self, obj):
        return obj.termo_adocao # Mostra o nome do termo menor
    exibir_short_descrip_termo.boolean = True
    exibir_short_descrip_termo.short_description = 'Termo'


    

    # Método para exibir o status de adoção do pet no AdotanteAdmin
    def status_adocao(self, obj):
        return "Aprovada" if obj.pet.adotado else "Não aprovada"
    
    status_adocao.short_description = 'Status da Adoção'


    #actions para aprovar, desaprovar e cancelar uma adoção

    # Ação para aprovar a adoção
    def aprovar_adocao(self, request, queryset):
        for adotante in queryset:
            adotante.pet.adotado = True
            adotante.pet.save()
        self.message_user(request, "Adoção aprovada com sucesso.")

    aprovar_adocao.short_description = "Aprovar adoção para o(s) pet(s) selecionado(s)"

    # Ação para desaprovar a adoção
    def desaprovar_adocao(self, request, queryset):
        for adotante in queryset:
            adotante.pet.adotado = False
            adotante.pet.save()
        self.message_user(request, "Adoção desaprovada com sucesso.")

    desaprovar_adocao.short_description = "Desaprovar adoção para o(s) pet(s) selecionado(s)"