from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User

# Create your models here.
class Client(TenantMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    on_trial = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass