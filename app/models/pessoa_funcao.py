# app/models/pessoa_funcao.py
from django.core.exceptions import ValidationError
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

    def clean(self):
        errors = {}

        # Pessoa obrigatória
        if not self.pessoa:
            errors['pessoa'] = "É necessário informar a pessoa."

        # Função obrigatória
        if not self.funcao:
            errors['funcao'] = "É necessário informar a função."

        # Verificar se função pertence a algum departamento
        if self.funcao and not self.funcao.departamento:
            errors['funcao'] = "A função deve pertencer a um departamento."

        if errors:
            raise ValidationError(errors)