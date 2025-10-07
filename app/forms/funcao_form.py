from django import forms
from app.models.funcao import Funcao

class FuncaoForm(forms.ModelForm):
    class Meta:
        model = Funcao
        fields = ['nome', 'departamento', 'quantidade_por_evento']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade_por_evento': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
