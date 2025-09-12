from rest_framework import serializers
from app.models import Indisponibilidade

class IndisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indisponibilidade
        fields = '__all__'