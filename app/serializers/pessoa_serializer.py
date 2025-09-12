# app/serializers/pessoa_serializer.py
from rest_framework import serializers
from app.models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def validate(self, attrs):
        instance = Pessoa(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs