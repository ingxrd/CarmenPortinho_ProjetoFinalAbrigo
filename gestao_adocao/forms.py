
from django import forms
from .models import CandidatoAdocao

class CandidatoAdocaoForm(forms.ModelForm):
     class Meta:
        model = CandidatoAdocao
        fields = ['nome', 'cpf', 'telefone', 'email', 'idade', 'termo_adocao', 'data_criacao', 'pet']
