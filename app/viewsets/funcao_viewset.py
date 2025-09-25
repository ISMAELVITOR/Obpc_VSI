from rest_framework import viewsets
from app.models import Funcao
from app.serializers.funcao_serializer import FuncaoSerializer
from app.permissions import FuncaoPermission

class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer
    permission_classes = [FuncaoPermission]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Funcao.objects.all()
        
        # Para líder: funções dos departamentos onde é líder
        if user.perfil == "lider":
            from app.models import Departamento
            departamentos_lider = Departamento.objects.filter(lider=user)
            return Funcao.objects.filter(departamento__in=departamentos_lider)
        
        # Para membro: funções dos departamentos onde tem funções
        from app.models import PessoaFuncao
        departamentos_ids = PessoaFuncao.objects.filter(
            pessoa=user
        ).values_list('funcao__departamento_id', flat=True).distinct()
        
        return Funcao.objects.filter(departamento_id__in=departamentos_ids)

