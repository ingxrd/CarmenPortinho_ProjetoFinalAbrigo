
from django import forms
from gestao_adocao.models import Adotante

class AdotanteForm(forms.ModelForm):
     class Meta:
        model = Adotante
        fields = ['nome', 'cpf', 'telefone', 'email', 'idade', 'termo_adocao', 'pet']
