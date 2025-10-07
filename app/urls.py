from django.urls import path
from app.views import pessoa_view 
from app.views import funcao_view
from app.views import departamento_view
from app.views import indisponibilidade_view
from app.views import evento_view
from app.views import escala_view
from app.views import pessoa_funcao_view
from app.views import home_view


from app.views.auth_views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    # Pessoa
    path('pessoas/', pessoa_view.PessoaListView.as_view(), name='listar_pessoas'),
    path('pessoas/criar/', pessoa_view.PessoaCreateView.as_view(), name='criar_pessoa'),
    path('pessoas/<int:pk>/editar/', pessoa_view.PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('pessoas/<int:pk>/deletar/', pessoa_view.PessoaDeleteView.as_view(), name='deletar_pessoa'),
    # Funcao
    path("funcoes/", funcao_view.FuncaoListView.as_view(), name="listar_funcao"),
    path("funcoes/criar/", funcao_view.FuncaoCreateView.as_view(), name="criar_funcao"),
    path("funcoes/<int:pk>/editar/", funcao_view.FuncaoUpdateView.as_view(), name="editar_funcao"),
    path("funcoes/<int:pk>/deletar/", funcao_view.FuncaoDeleteView.as_view(), name="deletar_funcao"),
    # Departamento
    path('departamentos/', departamento_view.DepartamentoListView.as_view(), name='listar_departamento'),
    path('departamentos/criar/', departamento_view.DepartamentoCreateView.as_view(), name='criar_departamento'),
    path('departamentos/<int:pk>/editar/', departamento_view.DepartamentoUpdateView.as_view(), name='editar_departamento'),
    path('departamentos/<int:pk>/deletar/', departamento_view.DepartamentoDeleteView.as_view(), name='deletar_departamento'),
    # Indisponibilidade
    path("indisponibilidades/", indisponibilidade_view.IndisponibilidadeListView.as_view(), name="listar_indisponibilidade"),
    path("indisponibilidades/criar/", indisponibilidade_view.IndisponibilidadeCreateView.as_view(), name="criar_indisponibilidade"),
    path("indisponibilidades/<int:pk>/editar/", indisponibilidade_view.IndisponibilidadeUpdateView.as_view(), name="editar_indisponibilidade"),
    path("indisponibilidades/<int:pk>/deletar/", indisponibilidade_view.IndisponibilidadeDeleteView.as_view(), name="deletar_indisponibilidade"),
    # Evento
    path("eventos/", evento_view.EventoListView.as_view(), name="listar_evento"),
    path("eventos/criar/", evento_view.EventoCreateView.as_view(), name="criar_evento"),
    path("eventos/<int:pk>/editar/", evento_view.EventoUpdateView.as_view(), name="editar_evento"),
    path("eventos/<int:pk>/deletar/", evento_view.EventoDeleteView.as_view(), name="deletar_evento"),
    # Escala
    path('escalas/', escala_view.EscalaListView.as_view(), name='listar_escala'),
    path('escalas/criar/', escala_view.EscalaCreateView.as_view(), name='criar_escala'),
    path('escalas/<int:pk>/editar/', escala_view.EscalaUpdateView.as_view(), name='editar_escala'),
    path('escalas/<int:pk>/deletar/', escala_view.EscalaDeleteView.as_view(), name='deletar_escala'),
    # PessoaFunção
    path('pessoa-funcao/', pessoa_funcao_view.PessoaFuncaoListView.as_view(), name='listar_pessoa_funcao'),
    path('pessoa-funcao/criar/', pessoa_funcao_view.PessoaFuncaoCreateView.as_view(), name='criar_pessoa_funcao'),
    path('pessoa-funcao/<int:pk>/editar/', pessoa_funcao_view.PessoaFuncaoUpdateView.as_view(), name='editar_pessoa_funcao'),
    path('pessoa-funcao/<int:pk>/deletar/', pessoa_funcao_view.PessoaFuncaoDeleteView.as_view(), name='deletar_pessoa_funcao'),
    # login
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    # tela inicial
    path('', home_view.HomeView.as_view(), name='home'),
]
