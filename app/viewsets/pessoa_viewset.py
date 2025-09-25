from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Pessoa
from app.serializers.pessoa_serializer import PessoaSerializer
from app.permissions import IsAdmin, IsLider, IsMembro


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
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
            return Pessoa.objects.all()
        elif user.perfil == "lider":
            return Pessoa.objects.filter(departamento=user.departamento)
        return Pessoa.objects.filter(id=user.id)
