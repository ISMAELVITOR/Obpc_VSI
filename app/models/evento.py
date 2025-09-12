from django.db import models

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