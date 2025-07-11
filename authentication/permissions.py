from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'
