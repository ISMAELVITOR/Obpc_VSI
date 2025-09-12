# app/serializers/departamento_serializer.py
from rest_framework import serializers
from app.models import Departamento
import re

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

    def validate_nome(self, value):
        """Verifica se o nome contém apenas letras e espaços"""
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', value):
            raise serializers.ValidationError("O nome do departamento deve conter apenas letras e espaços.")
        return value

    def validate(self, attrs):
        """Valida lider e duplicidade de departamento"""
        lider = attrs.get('lider')
        nome = attrs.get('nome')

        if lider is None:
            raise serializers.ValidationError({"lider": "O departamento deve ter um líder definido."})

        # Verifica duplicidade de nome
        if Departamento.objects.filter(nome=nome).exists():
            raise serializers.ValidationError({"nome": f"Já existe um departamento com o nome '{nome}'."})

        return attrs
