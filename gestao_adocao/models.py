# import uuid
# from django.db import models
# from django.utils import timezone
# from cadastro_pet.models import Pet


# class CandidatoAdocao(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nome = models.CharField(max_length=50)
#     cpf = models.CharField(max_length=20)
#     telefone = models.CharField(max_length=30)
#     email = models.EmailField(max_length=50, unique=True)
#     data_criacao = models.DateTimeField(auto_now_add=True)
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='candidatos')

#     def clean(self):
#         if not self:
#             raise ValidationError("Candidato não aprovado para adoção.")

#     def __str__(self):
#         return f'{self.nome}, {self.email}, {self.telefone}'

#     class Meta:
#         verbose_name = 'Formulário de Candidato a Adoção'
#         verbose_name_plural = 'Formulários de Candidatos a Adoção'
#         ordering = ['data_criacao']