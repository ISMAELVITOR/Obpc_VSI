from rest_framework import viewsets
from app.models import Indisponibilidade
from app.serializers.indisponibilidade_serializer import IndisponibilidadeSerializer
from app.permissions import IndisponibilidadePermission

class IndisponibilidadeViewSet(viewsets.ModelViewSet):
    queryset = Indisponibilidade.objects.all()
    serializer_class = IndisponibilidadeSerializer
    permission_classes = [IndisponibilidadePermission]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Indisponibilidade.objects.all()
        
        # Para líder: indisponibilidades de pessoas no departamento do líder
        if user.perfil == "lider":
            from app.models import Departamento, PessoaFuncao
            departamentos_lider = Departamento.objects.filter(lider=user)
            pessoas_ids = PessoaFuncao.objects.filter(
                funcao__departamento__in=departamentos_lider
            ).values_list('pessoa_id', flat=True).distinct()
            
            return Indisponibilidade.objects.filter(pessoa_id__in=pessoas_ids)
        
        # Para membro: apenas as próprias indisponibilidades
        return Indisponibilidade.objects.filter(pessoa=user)
