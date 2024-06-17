from django.shortcuts import redirect
from functools import wraps
from django_tenants.utils import schema_context
from tenant.models import Client
from django.http import HttpResponseForbidden

def get_current_tenant(request):
    # This function should return the current tenant based on the request.
    # Assuming you identify the tenant by subdomain or some other logic.
    subdomain = request.get_host().split('.')[0]
    return subdomain

def owner_only(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        subdomain = get_current_tenant(request)
        with schema_context('public'):
            try:
                tenant = Client.objects.get(schema_name=subdomain)
                if tenant.user == request.user:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("You do not have permission to access this area.")
            except Client.DoesNotExist:
                return HttpResponseForbidden("Tenant does not exist.")
    return wrapper_func
