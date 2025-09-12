# app/models/pessoa.py
import re
from django.core.exceptions import ValidationError
from django.db import models
from validate_docbr import CPF as ValidadorCPF

class Pessoa(models.Model):
    PERFIL_CHOICES = [
        ("admin", "Administrador"),
        ("lider", "Líder"),
        ("membro", "Membro"),
    ]

    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    perfil = models.CharField(max_length=10, choices=PERFIL_CHOICES, default="membro")

    def __str__(self):
        return f"{self.nome} ({self.perfil})"

    def clean(self):
        errors = {}

        # Nome
        if not re.match(r'^[A-Za-zÀ-ÿ ]+$', self.nome):
            errors['nome'] = "O nome deve conter apenas letras e espaços."

        # CPF
        cpf_validator = ValidadorCPF()
        if not cpf_validator.validate(self.cpf):
            errors['cpf'] = "CPF inválido."

        # RG
        if self.rg and not re.fullmatch(r'\d{7}', self.rg):
            errors['rg'] = "O RG deve conter exatamente 7 dígitos numéricos."

        # Senha
        senha = self.senha
        if len(senha) < 5 or \
           not re.search(r'[A-Z]', senha) or \
           not re.search(r'[a-z]', senha) or \
           not re.search(r'\d', senha) or \
           not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            errors['senha'] = ("A senha deve ter pelo menos 5 caracteres, "
                               "uma letra maiúscula, uma minúscula, um número e um caractere especial.")

        # Perfil
        if self.perfil not in dict(self.PERFIL_CHOICES):
            errors['perfil'] = "Perfil inválido."

        if errors:
            raise ValidationError(errors)

