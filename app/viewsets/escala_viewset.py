from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Escala
from app.serializers.escala_serializer import EscalaSerializer
from app.permissions import IsAdmin, IsLider, IsMembro


class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer
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
            return Escala.objects.all()
        elif user.perfil == "lider":
            return Escala.objects.filter(departamento=user.departamento)
        return Escala.objects.filter(departamento=user.departamento, pessoas=user)


