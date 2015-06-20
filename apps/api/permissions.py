from rest_framework.permissions import BasePermission


class UserRegistrationAPIPermission(BasePermission):

    def has_permission(self, request, view):
        p = request.META.get('HTTP_WP_API_KEY', None)
        from django.conf import settings
        if p == settings.REGISTRATION_API_KEY:
            return True
        else:
            return False


class PublisherAPIPermission(BasePermission):

    def has_permission(self, request, view):
        company = getattr(request, 'publisher', False)
        if company:
            return True
        return False
