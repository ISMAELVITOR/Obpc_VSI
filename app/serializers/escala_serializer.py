# app/serializers/escala_serializer.py
from rest_framework import serializers
from app.models import Escala

class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = '__all__'

    def validate(self, attrs):
        instance = Escala(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs
