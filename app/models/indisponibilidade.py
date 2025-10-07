# app/models/indisponibilidade.py
from django.core.exceptions import ValidationError
from django.db import models
from .pessoa import Pessoa
from datetime import date

class Indisponibilidade(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="indisponibilidades")
    data = models.DateField()

    class Meta:
        unique_together = ("pessoa", "data")

    def __str__(self):
        return f"{self.pessoa.nome} indisponível em {self.data}"

    def clean(self):
        errors = {}

        # Data não pode ser no passado
        if self.data < date.today():
            errors['data'] = "A data de indisponibilidade não pode ser no passado."

        # Pessoa obrigatória
        if not self.pessoa:
            errors['pessoa'] = "A indisponibilidade deve estar associada a uma pessoa."

        if errors:
            raise ValidationError(errors)