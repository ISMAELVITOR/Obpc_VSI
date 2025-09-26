from rest_framework import serializers
from app.models import Indisponibilidade

class IndisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indisponibilidade
        fields = ['id', 'data', 'pessoa']  # ou os campos que você tem
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove o campo pessoa do formulário para não-admin
        request = self.context.get('request')
        if request and request.user.perfil != 'admin':
            self.fields.pop('pessoa', None)
    
    def create(self, validated_data):
        # Para não-admin, força a pessoa ser o usuário logado
        request = self.context.get('request')
        if request and request.user.perfil != 'admin':
            validated_data['pessoa'] = request.user
        return super().create(validated_data)
