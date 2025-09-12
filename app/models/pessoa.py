from django.db import models

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
    senha = models.CharField(max_length=128)  # pode aplicar hash depois
    perfil = models.CharField(max_length=10, choices=PERFIL_CHOICES, default="membro")

    def __str__(self):
        return f"{self.nome} ({self.perfil})"

