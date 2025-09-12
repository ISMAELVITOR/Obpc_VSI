# app/serializers/funcao_serializer.py
from rest_framework import serializers
from app.models import Funcao

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'

    def validate(self, attrs):
        instance = Funcao(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return attrs