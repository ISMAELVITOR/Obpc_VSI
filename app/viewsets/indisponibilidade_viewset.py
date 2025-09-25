from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Indisponibilidade
from app.serializers.indisponibilidade_serializer import IndisponibilidadeSerializer
from app.permissions import IsAdmin, IsLider, IsMembro


class IndisponibilidadeViewSet(viewsets.ModelViewSet):
    queryset = Indisponibilidade.objects.all()
    serializer_class = IndisponibilidadeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.user.perfil == "admin":
            return [IsAdmin()]
        elif self.request.user.perfil == "lider":
            return [IsLider()]
        return [IsMembro()]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Indisponibilidade.objects.all()
        elif user.perfil == "lider":
            return Indisponibilidade.objects.filter(pessoa__departamento=user.departamento)
        return Indisponibilidade.objects.filter(pessoa=user)
