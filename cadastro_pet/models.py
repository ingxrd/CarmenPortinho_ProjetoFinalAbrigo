import uuid
from django.utils import timezone
from django.db import models

class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    nome_pet = models.CharField(max_length=50, blank=False) 
    idade_pet = models.CharField(max_length=20, blank=False)
    raca_pet = models.CharField(max_length=30, blank=False)
    imagem = models.ImageField(upload_to='fotos-pets/')  
    data_criacao = models.DateTimeField(auto_now_add=True)
    adotado = models.BooleanField(default=False)

    ESPECIES_CHOICES = [
        ("gato", "Gato"),
        ("cachorro", "Cachorro"),
    ]
    
    especie_pet = models.CharField(max_length=10, choices=ESPECIES_CHOICES, blank=False)  

    historico_saude = models.TextField(blank=True)  

    #Parte do painel administrativo

    #Essa parte diz: o Pet vai ser uma string e lá no painel administrativo, vai aparecer o id, nome e imagem
    # def __str__(self):
    #     return f'{self.id}, {self.nome_pet}, {self.imagem}'
    
    #Diz como as informações da tabela de pets serão apresentadas no painel administrativo do Django
    class Meta:
        verbose_name = 'Formulário Novo Pet'
        verbose_name_plural = 'Formulários de pets'
        ordering = ['data_criacao']