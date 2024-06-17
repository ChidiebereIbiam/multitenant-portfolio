from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django_tenants.utils import schema_context

User = get_user_model()

class PublicSchemaBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        with schema_context('public'):
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        with schema_context('public'):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None
