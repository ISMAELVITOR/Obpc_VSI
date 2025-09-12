from rest_framework import viewsets
from app.models import Evento
from app.serializers.evento_serializer import EventoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer