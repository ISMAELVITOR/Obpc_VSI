# app/models/escala.py
from django.core.exceptions import ValidationError
from django.db import models
from .evento import Evento
from .pessoa import Pessoa
from .funcao import Funcao
from datetime import date

class Escala(models.Model):
    mes = models.IntegerField()
    ano = models.IntegerField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="escalas")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="escalas")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name="escalas")
    data = models.DateField()

    class Meta:
        unique_together = ("evento", "pessoa", "funcao", "data")

    def __str__(self):
        return f"{self.evento.nome} - {self.funcao.nome} - {self.pessoa.nome} ({self.data})"

    def clean(self):
        errors = {}

        # Data
        if self.data < date.today():
            errors['data'] = "A data da escala não pode ser no passado."

        # Pessoa, função e evento obrigatórios
        if not self.pessoa:
            errors['pessoa'] = "A escala deve ter uma pessoa atribuída."
        if not self.funcao:
            errors['funcao'] = "A escala deve ter uma função atribuída."
        if not self.evento:
            errors['evento'] = "A escala deve estar associada a um evento."

        # Checar consistência de mês e ano
        if self.mes < 1 or self.mes > 12:
            errors['mes'] = "Mês inválido."
        if self.ano < 2000 or self.ano > 2100:
            errors['ano'] = "Ano inválido."

        if errors:
            raise ValidationError(errors)