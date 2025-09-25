from rest_framework import viewsets
from app.models import Pessoa
from app.serializers.pessoa_serializer import PessoaSerializer
from app.permissions import PessoaPermission

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [PessoaPermission]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Pessoa.objects.all()
        
        # Para líder: pessoas que têm funções no mesmo departamento que o líder
        if user.perfil == "lider":
            from app.models import PessoaFuncao, Departamento
            
            # Encontra os departamentos onde o usuário é líder
            departamentos_lider = Departamento.objects.filter(lider=user)
            # Pessoas que têm funções nesses departamentos
            pessoas_ids = PessoaFuncao.objects.filter(
                funcao__departamento__in=departamentos_lider
            ).values_list('pessoa_id', flat=True).distinct()
            
            return Pessoa.objects.filter(id__in=pessoas_ids)
        
        # Para membro: apenas o próprio usuário
        return Pessoa.objects.filter(id=user.id)

