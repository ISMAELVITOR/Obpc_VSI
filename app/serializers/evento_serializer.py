# app/serializers/evento_serializer.py
from rest_framework import serializers
from app.models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

    def validate(self, attrs):
        instance = Evento(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs