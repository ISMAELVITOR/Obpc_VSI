# app/serializers/pessoa_funcao_serializer.py
from rest_framework import serializers
from app.models import PessoaFuncao
from django.core.exceptions import ValidationError

class PessoaFuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaFuncao
        fields = '__all__'

    def validate(self, attrs):
        instance = PessoaFuncao(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs