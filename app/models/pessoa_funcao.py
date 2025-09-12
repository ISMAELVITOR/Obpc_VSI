from django.db import models
from .pessoa import Pessoa
from .funcao import Funcao

class PessoaFuncao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="funcoes_pessoa")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name="pessoas_funcao")

    class Meta:
        unique_together = ("pessoa", "funcao")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.funcao.nome}"