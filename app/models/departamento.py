# app/models/departamento.py
from django.core.exceptions import ValidationError
from django.db import models
from .pessoa import Pessoa
import re

class Departamento(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    lider = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, related_name="departamentos_lider")

    def __str__(self):
        return self.nome

    def clean(self):
        errors = {}

        # Nome
        if not re.match(r'^[A-Za-zÀ-ÿ ]+$', self.nome):
            errors['nome'] = "O nome do departamento deve conter apenas letras e espaços."

        # Líder
        if not self.lider:
            errors['lider'] = "Um departamento deve ter um líder."

        if errors:
            raise ValidationError(errors)