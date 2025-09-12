from rest_framework import viewsets
from app.models import Escala
from app.serializers.escala_serializer import EscalaSerializer

class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer