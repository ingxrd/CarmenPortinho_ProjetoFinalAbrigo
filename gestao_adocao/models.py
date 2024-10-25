import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from cadastro_pet.models import Pet



class Adotante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)  
    telefone = models.CharField(max_length=15)  
    email = models.EmailField(max_length=50, unique=True)
    idade = models.BooleanField(default=False, verbose_name='Sua idade é maior de 18 anos?')
    termo_adocao = models.BooleanField(default=False, verbose_name='Você concorda com os termos de adoção responsável?')
    data_criacao = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='candidatos')

    def clean(self):
        if not self.nome or not self.cpf or not self.telefone or not self.email:
            raise ValidationError("Todos os campos são obrigatórios.")
        
        # Validação do CPF
        if not self.validar_cpf(self.cpf):
            raise ValidationError("CPF inválido.")

    def validar_cpf(self, cpf):
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais (caso '111.111.111-11', por exemplo)
        if cpf == cpf[0] * len(cpf):
            return False

        # Cálculo do primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = (soma * 10) % 11
        primeiro_digito = 0 if primeiro_digito == 10 else primeiro_digito

        # Cálculo do segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        segundo_digito = (soma * 10) % 11
        segundo_digito = 0 if segundo_digito == 10 else segundo_digito

        # Verifica se os dígitos verificadores estão corretos
        return cpf[-2:] == f'{primeiro_digito}{segundo_digito}'

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.telefone}'

    class Meta:
        verbose_name = 'Formulário de Candidato a Adoção'
        verbose_name_plural = 'Formulários de Candidatos a Adoção'
        ordering = ['data_criacao']
