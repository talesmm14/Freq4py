from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        if request.method == "GET":
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.created_by == request.user
