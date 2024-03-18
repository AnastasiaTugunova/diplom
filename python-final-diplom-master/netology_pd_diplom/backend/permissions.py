from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as ms


class IsShopsReadOnly(BasePermission):
    message = ms("Permission")

    def has_permission(self, request, view):
        return request.user.type == 'shop'
