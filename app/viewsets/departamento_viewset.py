from rest_framework import viewsets
from app.models import Departamento
from app.serializers.departamento_serializer import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer