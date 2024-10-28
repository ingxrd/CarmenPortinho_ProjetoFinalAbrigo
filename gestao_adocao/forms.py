from django import forms
from .models import Adotante  # Apenas importando Adotante, sem qualquer importação de models.py no sentido contrário.

class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = ['nome', 'cpf', 'telefone', 'email', 'pet', 'idade', 'termo_adocao']
