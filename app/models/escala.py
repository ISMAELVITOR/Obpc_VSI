from django.db import models
from .evento import Evento
from .pessoa import Pessoa
from .funcao import Funcao

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