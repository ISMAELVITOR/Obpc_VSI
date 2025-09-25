from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """Apenas Admin tem acesso total"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == "admin"

    def has_object_permission(self, request, view, obj):
        return True


class IsLider(BasePermission):
    """Líder tem acesso ao seu próprio departamento"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == "lider"

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "departamento"):
            return obj.departamento == request.user.departamento
        return True


class IsMembro(BasePermission):
    """Membro só pode ver e editar seus próprios dados"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == "membro"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # Pode visualizar coisas do mesmo departamento
            if hasattr(obj, "departamento"):
                return obj.departamento == request.user.departamento
            return True
        # Para edição, só pode mexer em si mesmo
        return obj == request.user



