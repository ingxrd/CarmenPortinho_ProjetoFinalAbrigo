from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# Importação das views

from home.views import home, adote_pet
from cadastro_pet.views import criar_pet
from detalhes_pet.views import detalhes_pet
from gestao_adocao.views import adote_view
from gestao_adocao.views import remover_adocao



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastrar-pet/', criar_pet),
    path('detalhes/<uuid:id>/', detalhes_pet, name='detalhes_pet'),
    path('adote/', adote_pet, name = 'adote'), #junto com a listagem dos bicinhos disponiveis e a barra de pesquisa
    path('/formulario_adocao', adote_view, name='adote_view'),
    path('/formulario_adocao', remover_adocao, name='remover_adocao')

    #Falta:
    #Formulário de Adoção
    #Sobre => espaço para apresentação da Squad

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)