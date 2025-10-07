from django import forms
from app.models.departamento import Departamento
from app.models.pessoa import Pessoa

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'lider']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'lider': forms.Select(attrs={'class': 'form-control'}),
        }
