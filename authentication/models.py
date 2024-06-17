from django.contrib.auth.models import AbstractUser
from django_tenants.utils import schema_context

class User(AbstractUser):
    def save(self, *args, **kwargs):
        with schema_context('public'):
            super().save(*args, **kwargs)