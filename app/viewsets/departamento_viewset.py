from rest_framework import viewsets
from app.models import Departamento
from app.serializers.departamento_serializer import DepartamentoSerializer
from app.permissions import DepartamentoPermission

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [DepartamentoPermission]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Departamento.objects.all()
        
        # Para líder: visualiza todos os departamentos
        if user.perfil == "lider":
            return Departamento.objects.all()
        
        # Para membro: departamentos onde o usuário tem funções
        from app.models import PessoaFuncao
        departamentos_ids = PessoaFuncao.objects.filter(
            pessoa=user
        ).values_list('funcao__departamento_id', flat=True).distinct()
        
        return Departamento.objects.filter(id__in=departamentos_ids)


