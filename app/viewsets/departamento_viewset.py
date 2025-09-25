from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Departamento
from app.serializers.departamento_serializer import DepartamentoSerializer
from app.permissions import IsAdmin, IsLider


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.user.perfil == "admin":
            return [IsAdmin()]
        return [IsLider()]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Departamento.objects.all()
        return Departamento.objects.filter(id=user.departamento_id)

