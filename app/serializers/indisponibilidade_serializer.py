# app/serializers/indisponibilidade_serializer.py
from rest_framework import serializers
from app.models import Indisponibilidade

class IndisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indisponibilidade
        fields = '__all__'

    def validate(self, attrs):
        instance = Indisponibilidade(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs