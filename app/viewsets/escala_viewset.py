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
        
        # Para líder: escalas dos departamentos onde é líder
        if user.perfil == "lider":
            from app.models import Departamento
            departamentos_lider = Departamento.objects.filter(lider=user)
            return Escala.objects.filter(departamento__in=departamentos_lider)
        
        # Para membro: escalas onde está incluído como pessoa (campo correto: pessoa)
        return Escala.objects.filter(pessoa=user)



