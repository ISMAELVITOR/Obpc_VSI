# app/models/funcao.py
from django.core.exceptions import ValidationError
from django.db import models
from .departamento import Departamento
import re

class Funcao(models.Model):
    nome = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="funcoes")

    class Meta:
        unique_together = ('nome', 'departamento')

    def __str__(self):
        return f"{self.nome} ({self.departamento.nome})"

    def clean(self):
        errors = {}

        # Nome
        if not re.match(r'^[A-Za-zÀ-ÿ ]+$', self.nome):
            errors['nome'] = "O nome da função deve conter apenas letras e espaços."

        # Departamento
        if not self.departamento:
            errors['departamento'] = "A função deve estar associada a um departamento."

        if errors:
            raise ValidationError(errors)