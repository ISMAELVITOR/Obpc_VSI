from django.core.exceptions import ValidationError
from django.db import models
from .evento import Evento
from .pessoa import Pessoa
from .funcao import Funcao
from .pessoa_funcao import PessoaFuncao
from datetime import date

class Escala(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="escalas")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="escalas")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name="escalas")

    class Meta:
        unique_together = ("evento", "pessoa", "funcao")  # garante que não haja duplicidade

    def __str__(self):
        return f"{self.evento.nome} - {self.funcao.nome} - {self.pessoa.nome} ({self.evento.data_inicio})"

    def clean(self):
        errors = {}

        # Validação da data do evento
        if self.evento.data_inicio < date.today():
            errors['evento'] = "Não é possível criar uma escala para evento no passado."

        # Pessoa, função e evento obrigatórios
        if not self.pessoa:
            errors['pessoa'] = "A escala deve ter uma pessoa atribuída."
        if not self.funcao:
            errors['funcao'] = "A escala deve ter uma função atribuída."
        if not self.evento:
            errors['evento'] = "A escala deve estar associada a um evento."

        # Validar se a pessoa possui essa função
        if self.pessoa and self.funcao:
            possui_funcao = PessoaFuncao.objects.filter(pessoa=self.pessoa, funcao=self.funcao).exists()
            if not possui_funcao:
                errors['funcao'] = "Esta pessoa não possui a função selecionada."

        if errors:
            raise ValidationError(errors)

