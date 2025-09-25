from rest_framework import serializers
from django.core.exceptions import ValidationError
from app.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Pessoa
        fields = [
            "id",
            "nome",
            "data_nascimento",
            "cpf",
            "rg",
            "email",
            "perfil",
            "senha",  # só entrada, nunca saída
        ]

    def validate(self, attrs):
        instance = Pessoa(**{k: v for k, v in attrs.items() if k != "senha"})
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs

    def create(self, validated_data):
        senha = validated_data.pop("senha", None)
        groups = validated_data.pop("groups", [])  # captura os grupos enviados
        user = Pessoa(**validated_data)
        if senha:
            user.set_password(senha)
        user.save()
        if groups:
            user.groups.set(groups)  # atribui depois do save
        return user

    def update(self, instance, validated_data):
        senha = validated_data.pop("senha", None)
        groups = validated_data.pop("groups", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if senha:
            instance.set_password(senha)
        instance.save()
        if groups is not None:
            instance.groups.set(groups)
        return instance


