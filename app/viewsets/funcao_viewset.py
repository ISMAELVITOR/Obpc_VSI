from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Funcao
from app.serializers.funcao_serializer import FuncaoSerializer
from app.permissions import IsAdmin, IsLider


class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.user.perfil == "admin":
            return [IsAdmin()]
        # Líder pode cadastrar funções só do próprio departamento
        return [IsLider()]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Funcao.objects.all()
        return Funcao.objects.filter(departamento=user.departamento)
