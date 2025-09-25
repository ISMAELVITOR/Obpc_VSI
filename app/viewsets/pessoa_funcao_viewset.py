from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import PessoaFuncao
from app.serializers.pessoa_funcao_serializer import PessoaFuncaoSerializer
from app.permissions import IsAdmin, IsLider, IsMembro


class PessoaFuncaoViewSet(viewsets.ModelViewSet):
    queryset = PessoaFuncao.objects.all()
    serializer_class = PessoaFuncaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return PessoaFuncao.objects.all()
        elif user.perfil == "lider":
            return PessoaFuncao.objects.filter(pessoa__departamento=user.departamento)
        else:  # membro
            return PessoaFuncao.objects.filter(pessoa=user)

    def get_permissions(self):
        if self.request.user.perfil == "membro":
            return [IsAuthenticated(), SomenteLeitura()]  # bloqueia POST/PUT/DELETE
        return [IsAuthenticated()]
