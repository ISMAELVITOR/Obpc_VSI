from django.db import models
from .pessoa import Pessoa

class Indisponibilidade(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="indisponibilidades")
    data = models.DateField()

    class Meta:
        unique_together = ("pessoa", "data")

    def __str__(self):
        return f"{self.pessoa.nome} indisponível em {self.data}"