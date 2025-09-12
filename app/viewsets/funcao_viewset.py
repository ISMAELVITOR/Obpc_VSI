from rest_framework import viewsets
from app.models import Funcao
from app.serializers.funcao_serializer import FuncaoSerializer

class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer