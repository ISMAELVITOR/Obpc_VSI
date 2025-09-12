from django.db import models
from .pessoa import Pessoa

class Departamento(models.Model):
    nome = models.CharField(max_length=255)
    lider = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, related_name="departamentos_lider")

    def __str__(self):
        return self.nome