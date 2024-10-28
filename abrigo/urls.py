from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importação das views

from home.views import home, adote_pet, sobre, contato
from cadastro_pet.views import criar_pet
from detalhes_pet.views import detalhes_pet
from gestao_adocao.views import criar_adocao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastrar-pet/', criar_pet),
    path('detalhes/<uuid:id>/', detalhes_pet, name='detalhes_pet'),
    path('adote/', adote_pet, name = 'adote'), 
    path('criar_adocao/', criar_adocao, name='criar_adocao'),  
    # path('listar_adocoes/', listar_adocoes, name='listar_adocoes'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato')
    
    #Sobre => espaço para apresentação da Squad

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)