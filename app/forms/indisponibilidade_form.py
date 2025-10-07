from django import forms
from app.models.indisponibilidade import Indisponibilidade

class IndisponibilidadeForm(forms.ModelForm):
    class Meta:
        model = Indisponibilidade
        fields = ['pessoa', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
