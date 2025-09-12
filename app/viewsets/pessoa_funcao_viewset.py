from rest_framework import viewsets
from app.models import PessoaFuncao
from app.serializers.pessoa_funcao_serializer import PessoaFuncaoSerializer

class PessoaFuncaoViewSet(viewsets.ModelViewSet):
    queryset = PessoaFuncao.objects.all()
    serializer_class = PessoaFuncaoSerializer