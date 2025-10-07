# app/models/evento.py
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date

class Evento(models.Model):
    RECORRENCIA_CHOICES = [
        ("nenhuma", "Nenhuma"),
        ("semanal", "Semanal"),
        ("mensal", "Mensal"),
        ("anual", "Anual"),
    ]

    nome = models.CharField(max_length=255)
    data_inicio = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    recorrencia_tipo = models.CharField(max_length=10, choices=RECORRENCIA_CHOICES, default="nenhuma")
    recorrencia_dia_semana = models.IntegerField(blank=True, null=True)  # 0=domingo, 6=sábado
    recorrencia_fim = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.data_inicio})"

    def clean(self):
        errors = {}

        # Nome obrigatório
        if not self.nome.strip():
            errors['nome'] = "O nome do evento é obrigatório."

        # Data início
        if self.data_inicio < date.today():
            errors['data_inicio'] = "A data de início não pode ser no passado."

        # Hora início/fim
        if self.hora_fim <= self.hora_inicio:
            errors['hora_fim'] = "A hora de fim deve ser depois da hora de início."

        # Recorrência semanal precisa de dia da semana
        if self.recorrencia_tipo == "semanal" and self.recorrencia_dia_semana is None:
            errors['recorrencia_dia_semana'] = "Escolha o dia da semana para eventos semanais."

        # Recorrência fim precisa ser depois da data início
        if self.recorrencia_fim and self.recorrencia_fim <= self.data_inicio:
            errors['recorrencia_fim'] = "A data final da recorrência deve ser depois da data de início."

        if errors:
            raise ValidationError(errors)