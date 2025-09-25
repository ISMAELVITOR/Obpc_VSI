from rest_framework import viewsets
from app.models import PessoaFuncao
from app.serializers.pessoa_funcao_serializer import PessoaFuncaoSerializer
from app.permissions import PessoaFuncaoPermission

class PessoaFuncaoViewSet(viewsets.ModelViewSet):
    queryset = PessoaFuncao.objects.all()
    serializer_class = PessoaFuncaoSerializer
    permission_classes = [PessoaFuncaoPermission]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return PessoaFuncao.objects.all()
        
        # Para líder: funções das pessoas no departamento do líder
        if user.perfil == "lider":
            from app.models import Departamento
            departamentos_lider = Departamento.objects.filter(lider=user)
            return PessoaFuncao.objects.filter(
                funcao__departamento__in=departamentos_lider
            )
        
        # Para membro: apenas as próprias funções
        return PessoaFuncao.objects.filter(pessoa=user)

