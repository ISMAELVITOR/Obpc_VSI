# app/models/funcao.py
from django.db import models
from .departamento import Departamento

class Funcao(models.Model):
    nome = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="funcoes")

    class Meta:
        unique_together = ('nome', 'departamento')

    def __str__(self):
        return f"{self.nome} ({self.departamento.nome})"