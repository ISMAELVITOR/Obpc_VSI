from rest_framework.permissions import BasePermission, SAFE_METHODS


# ============================================================
# Permissões genéricas reutilizáveis
# ============================================================

class IsAdmin(BasePermission):
    """Apenas Admin tem acesso total"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == "admin"

    def has_object_permission(self, request, view, obj):
        return True  # Admin tem acesso irrestrito


class ReadOnly(BasePermission):
    """Permite apenas métodos de leitura (GET, HEAD, OPTIONS)"""
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsSelfOrAdmin(BasePermission):
    """
    Admin tem acesso total.
    Líder/Membro só podem ver/editar os próprios dados.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.perfil == "admin":
            return True
        return obj == request.user


class IsOwnOrAdmin(BasePermission):
    """
    Para objetos relacionados ao usuário (ex.: Indisponibilidade, PessoaFunção).
    Admin tem acesso a tudo.
    Usuário comum só vê os seus.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.perfil == "admin":
            return True

        # Se o objeto tem um campo pessoa, verifica se pertence ao usuário
        if hasattr(obj, "pessoa"):
            return obj.pessoa == request.user
        return False


# ============================================================
# Permissões específicas por recurso - CORRIGIDAS
# ============================================================

class DepartamentoPermission(BasePermission):
    """
    Admin pode criar/editar/excluir.
    Todos podem visualizar.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
            
        if request.method in SAFE_METHODS:
            return True
        return request.user.perfil == "admin"


class EventoPermission(BasePermission):
    """
    Admin pode criar/editar/excluir.
    Todos podem visualizar.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
            
        if request.method in SAFE_METHODS:
            return True
        return request.user.perfil == "admin"


class EscalaPermission(BasePermission):
    """
    Admin pode criar/editar/excluir.
    Todos podem visualizar.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
            
        if request.method in SAFE_METHODS:
            return True
        return request.user.perfil == "admin"


class PessoaPermission(BasePermission):
    """
    Admin pode gerenciar todos.
    Líder pode visualizar pessoas do seu departamento.
    Membro só pode ver/editar os próprios dados.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
            
        # Admin pode tudo
        if request.user.perfil == "admin":
            return True
            
        # Líder pode visualizar e criar pessoas no seu departamento
        if request.user.perfil == "lider":
            return True
            
        # Membro: pode criar se for através do registro (normalmente não) 
        # ou métodos seguros (GET) para ver próprio perfil
        # OU se for atualização do próprio usuário (isso será verificado no object_permission)
        if request.method in SAFE_METHODS or request.method in ['PUT', 'PATCH']:
            return True
            
        # Membro não pode criar outras pessoas (POST)
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.perfil == "admin":
            return True
            
        if request.user.perfil == "lider":
            # Líder pode gerenciar pessoas do seu departamento
            from app.models import PessoaFuncao, Departamento
            departamentos_lider = Departamento.objects.filter(lider=request.user)
            # Verifica se a pessoa tem funções no departamento do líder
            return PessoaFuncao.objects.filter(
                pessoa=obj, 
                funcao__departamento__in=departamentos_lider
            ).exists()
            
        # Membro só pode acessar os próprios dados (GET, PUT, PATCH)
        return obj == request.user


class IndisponibilidadePermission(BasePermission):
    """
    Admin pode gerenciar tudo.
    Líder pode ver indisponibilidades do seu departamento.
    Usuário só pode acessar/criar suas próprias indisponibilidades.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
            
        # Admin pode tudo
        if request.user.perfil == "admin":
            return True
            
        # Líder pode visualizar
        if request.user.perfil == "lider" and request.method in SAFE_METHODS:
            return True
            
        # Membro: pode criar própria indisponibilidade ou visualizar
        if request.method in SAFE_METHODS:
            return True
            
        # Para POST: membro só pode criar própria indisponibilidade
        if request.method == 'POST':
            # Verifica se está tentando criar uma indisponibilidade para si mesmo
            pessoa_id = request.data.get('pessoa')
            if pessoa_id:
                return str(pessoa_id) == str(request.user.id)
            # Se não especificar pessoa, assume que é para si mesmo
            return True
            
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.perfil == "admin":
            return True
            
        if request.user.perfil == "lider":
            # Líder pode ver indisponibilidades do seu departamento
            from app.models import PessoaFuncao, Departamento
            departamentos_lider = Departamento.objects.filter(lider=request.user)
            return PessoaFuncao.objects.filter(
                pessoa=obj.pessoa, 
                funcao__departamento__in=departamentos_lider
            ).exists()
            
        # Usuário só pode acessar suas próprias indisponibilidades
        return hasattr(obj, "pessoa") and obj.pessoa == request.user


class FuncaoPermission(BasePermission):
    """
    Admin pode criar/editar/excluir funções.
    Todos podem visualizar.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
            
        if request.method in SAFE_METHODS:
            return True
        return request.user.perfil == "admin"


class PessoaFuncaoPermission(BasePermission):
    """
    Admin pode gerenciar funções de qualquer pessoa.
    Líder pode gerenciar funções do seu departamento.
    Usuário só pode ver as suas próprias funções.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
            
        # Admin pode tudo
        if request.user.perfil == "admin":
            return True
            
        # Líder pode visualizar e criar funções no seu departamento
        if request.user.perfil == "lider":
            return True
            
        # Membro: só métodos seguros para ver próprias funções
        if request.method in SAFE_METHODS:
            return True
            
        # Membro não pode criar/editar/deletar funções de outras pessoas
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.perfil == "admin":
            return True
            
        if request.user.perfil == "lider":
            # Líder pode gerenciar funções do seu departamento
            from app.models import Departamento
            departamentos_lider = Departamento.objects.filter(lider=request.user)
            return obj.funcao.departamento in departamentos_lider
            
        # Usuário só pode acessar suas próprias funções
        return hasattr(obj, "pessoa") and obj.pessoa == request.user




