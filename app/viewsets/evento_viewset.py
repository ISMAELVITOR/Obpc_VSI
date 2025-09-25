from rest_framework import viewsets
from app.models import Evento
from app.serializers.evento_serializer import EventoSerializer
from app.permissions import EventoPermission

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EventoPermission]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == "admin":
            return Evento.objects.all()
        elif user.perfil == "lider":
            return Evento.objects.filter(departamento=user.departamento)
        return Evento.objects.all()



