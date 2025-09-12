from rest_framework import viewsets
from app.models import Pessoa
from app.serializers.pessoa_serializer import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer