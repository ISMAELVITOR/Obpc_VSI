from rest_framework import serializers
from validate_docbr import CPF
import re
from app.models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"
        extra_kwargs = {
            "senha": {"write_only": True},  # senha não aparece em GET
        }

    # ------------------------
    # Validações de campos
    # ------------------------

    def validate_nome(self, value):
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', value):
            raise serializers.ValidationError("O nome deve conter apenas letras e espaços.")
        return value

    def validate_cpf(self, value):
        cpf_validator = CPF()
        if not cpf_validator.validate(value):
            raise serializers.ValidationError("CPF inválido.")
        return value

    def validate_rg(self, value):
        if value and (not value.isdigit() or len(value) != 7):
            raise serializers.ValidationError("O RG deve conter exatamente 7 dígitos numéricos.")
        return value

    def validate_senha(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("A senha deve ter pelo menos 5 caracteres.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("A senha deve conter pelo menos uma letra minúscula.")
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("A senha deve conter pelo menos um número.")
        if not re.search(r'[@$!%*?&]', value):
            raise serializers.ValidationError("A senha deve conter pelo menos um caractere especial (@, $, !, %, *, ?, &).")
        return value