from rest_framework import permissions

class ProprietorshipPermission(permissions.BasePermission):
    """
    Permite el acceso solo si el usuario autenticado es el propietario del objeto.
    """
    def has_object_permission(self, request, view, obj):
        # Solo el propietario puede realizar acciones de lectura (GET).
        return obj == request.user