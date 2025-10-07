from django import forms
from app.models.evento import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data_inicio', 'hora_inicio', 'hora_fim', 
                  'recorrencia_tipo', 'recorrencia_dia_semana', 'recorrencia_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time'}),
            'recorrencia_fim': forms.DateInput(attrs={'type': 'date'}),
        }
