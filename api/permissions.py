from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if user is owner of object, `False` otherwise.
        """
        return bool(request.user and obj.user == request.user)

