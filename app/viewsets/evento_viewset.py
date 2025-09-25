from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Evento
from app.serializers.evento_serializer import EventoSerializer
from app.permissions import IsAdmin, IsLider, IsMembro


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
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
            return Evento.objects.all()
        elif user.perfil == "lider":
            return Evento.objects.filter(departamento=user.departamento)
        return Evento.objects.filter(departamento=user.departamento)
