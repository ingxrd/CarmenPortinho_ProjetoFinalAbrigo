from django.contrib import admin
from django.utils.safestring import mark_safe
from cadastro_pet.models import Pet 
# Register your models here.

@admin.register(Pet)
class CadastroAdmin(admin.ModelAdmin):
    #Quais campos irá aparecer no painel administrativo
    list_display = ['nome_pet', 'raca_pet', 'especie_pet', 'image_tag']
    search_fields = ['nome_pet', 'raca_pet', 'especie_pet']
    list_filter = ['data_criacao', 'nome_pet', 'especie_pet']

     # Exibir a imagem associada ao animal
    def image_tag(self, obj):
        # Verifica se o objeto (Pet) tem uma imagem associada
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" style="width: 100px; height: auto;" />')
        return "Sem imagem"
    
    image_tag.short_description = 'Imagem'