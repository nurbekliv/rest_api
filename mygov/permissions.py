from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, IsAdminUser


class IsAdminOrReadOnlyOrCreate(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            return True

        if request.method == 'POST':
            return True

        return False


class ReadOnlyOrCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return True
        return False


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

