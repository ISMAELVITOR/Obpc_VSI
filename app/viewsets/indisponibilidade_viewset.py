from rest_framework import viewsets
from app.models import Indisponibilidade
from app.serializers.indisponibilidade_serializer import IndisponibilidadeSerializer

class IndisponibilidadeViewSet(viewsets.ModelViewSet):
    queryset = Indisponibilidade.objects.all()
    serializer_class = IndisponibilidadeSerializer