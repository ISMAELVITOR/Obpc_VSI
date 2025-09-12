# app/serializers/funcao_serializer.py
from rest_framework import serializers
from app.models import Funcao
import re

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'

    def validate_nome(self, value):
        """Verifica se o nome da função contém apenas letras e espaços"""
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', value):
            raise serializers.ValidationError("O nome da função deve conter apenas letras e espaços.")
        return value

    def validate(self, attrs):
        """Valida departamento e duplicidade de função"""
        departamento = attrs.get('departamento')
        nome = attrs.get('nome')

        if departamento is None:
            raise serializers.ValidationError({"departamento": "A função deve pertencer a um departamento válido."})

        # Verifica duplicidade
        if Funcao.objects.filter(nome=nome, departamento=departamento).exists():
            raise serializers.ValidationError({"nome": f"Já existe uma função com o nome '{nome}' neste departamento."})

        return attrs