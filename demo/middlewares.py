
from django_tenants.middleware.main import TenantMainMiddleware
from django_tenants.utils import schema_context

class PublicSchemaMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        hostname = request.get_host().split(':')[0]
        if hostname == 'localhost':
            with schema_context('public'):
                super().process_request(request)
        else:
            super().process_request(request)