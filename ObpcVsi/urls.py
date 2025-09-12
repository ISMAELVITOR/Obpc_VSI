from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.viewsets import (
    DepartamentoViewSet,
    EventoViewSet,
    PessoaViewSet,
    FuncaoViewSet,
    IndisponibilidadeViewSet,
    EscalaViewSet,
    PessoaFuncaoViewSet,
)

router = routers.DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'pessoas', PessoaViewSet)
router.register(r'funcoes', FuncaoViewSet)
router.register(r'indisponibilidades', IndisponibilidadeViewSet)
router.register(r'escalas', EscalaViewSet)
router.register(r'pessoa-funcao', PessoaFuncaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


