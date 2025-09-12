from rest_framework import serializers
from app.models import PessoaFuncao

class PessoaFuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaFuncao
        fields = '__all__'