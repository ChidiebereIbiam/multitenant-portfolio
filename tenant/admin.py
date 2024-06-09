from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Client, Domain

# Register your models here.

class DomainInline(admin.TabularInline):
    model = Domain

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'address', 'paid_until')