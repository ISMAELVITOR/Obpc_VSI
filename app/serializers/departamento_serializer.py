# app/serializers/departamento_serializer.py
from rest_framework import serializers
from app.models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

    def validate(self, attrs):
        instance = Departamento(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs
