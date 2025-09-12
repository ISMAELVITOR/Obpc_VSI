from django.contrib import admin
from .models import (
    Departamento, Evento, Pessoa, Funcao,
    Indisponibilidade, Escala, PessoaFuncao
)

# Registro simples
admin.site.register(Departamento)
admin.site.register(Evento)
admin.site.register(Pessoa)
admin.site.register(Funcao)
admin.site.register(Indisponibilidade)
admin.site.register(Escala)
admin.site.register(PessoaFuncao)