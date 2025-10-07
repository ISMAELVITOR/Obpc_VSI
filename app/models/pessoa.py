import re
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from validate_docbr import CPF as ValidadorCPF


class PessoaManager(BaseUserManager):
    def create_user(self, email, nome, cpf, password=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um email")
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, cpf=cpf, **extra_fields)
        user.set_password(password)  # <- Garante hash correto
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cpf, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário precisa ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário precisa ter is_superuser=True.")

        return self.create_user(email, nome, cpf, password, **extra_fields)


class Pessoa(AbstractBaseUser, PermissionsMixin):
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
    perfil = models.CharField(max_length=10, choices=PERFIL_CHOICES, default="membro")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PessoaManager()

    USERNAME_FIELD = "email"           # login será feito por email
    REQUIRED_FIELDS = ["nome", "cpf", "data_nascimento"]  # campos obrigatórios além do email

    #def __str__(self):
     #   return f"{self.nome} ({self.perfil})"

    def __str__(self):
        return f"{self.nome} ({'admin' if self.is_superuser else 'usuário'})"
    
    def clean(self):
        """
        Valida os campos do modelo.
        """
        errors = {}

        # Nome: somente letras e espaços
        if not re.match(r'^[A-Za-zÀ-ÿ ]+$', self.nome):
            errors['nome'] = "O nome deve conter apenas letras e espaços."

        # CPF: válido e 11 dígitos
        cpf_validator = ValidadorCPF()
        if not cpf_validator.validate(self.cpf):
            errors['cpf'] = "CPF inválido."

        # RG: opcional, exatamente 7 dígitos se preenchido
        if self.rg and not re.fullmatch(r'\d{7}', self.rg):
            errors['rg'] = "O RG deve conter exatamente 7 dígitos numéricos."

        # Perfil
        if self.perfil not in dict(self.PERFIL_CHOICES):
            errors['perfil'] = "Perfil inválido."

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        """
        Sobrescreve o save para garantir que clean() seja chamado antes de salvar.
        """
        self.full_clean()  # chama clean() e valida campos
        super().save(*args, **kwargs)

