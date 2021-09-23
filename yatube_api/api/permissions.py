from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        verdict = (
            (request.method in permissions.SAFE_METHODS)
            or (obj.author == request.user))
        return verdict
