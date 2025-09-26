from rest_framework import viewsets
from app.models import Escala
from app.serializers.escala_serializer import EscalaSerializer
from app.permissions import EscalaPermission

class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer
    permission_classes = [EscalaPermission]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Escala.objects.all()
        
        # Para líder: escalas onde a pessoa escalada tem funções no departamento do líder
        if user.perfil == "lider":
            from app.models import PessoaFuncao, Departamento
            departamentos_lider = Departamento.objects.filter(lider=user)
            # Pessoas que têm funções nos departamentos do líder
            pessoas_ids = PessoaFuncao.objects.filter(
                funcao__departamento__in=departamentos_lider
            ).values_list('pessoa_id', flat=True).distinct()
            
            return Escala.objects.filter(pessoa_id__in=pessoas_ids)
        
        # Para membro: escalas onde está incluído como pessoa
        return Escala.objects.filter(pessoa=user)



