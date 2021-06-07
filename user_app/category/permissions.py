from rest_framework.permissions import BasePermission


class OnlyFirstNameAkashPermission(BasePermission):
    def has_permission(self, request, view):
        # return request.user.first_name == "Akash"
        return True
