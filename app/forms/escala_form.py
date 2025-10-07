from django import forms
from app.models.escala import Escala

class EscalaForm(forms.ModelForm):
    class Meta:
        model = Escala
        fields = ['evento', 'pessoa', 'funcao']

