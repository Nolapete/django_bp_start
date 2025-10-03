from django.db import connection
from apps.tenants.models import Tenant
from django.http import Http404
from rest_framework.exceptions import NotFound
from django.conf import settings


class RlsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hostname = request.get_host().split(":")[0].lower()

        request.tenant = None

        if hostname in ["127.0.0.1", "localhost"]:
            try:
                # Get the development tenant from settings
                dev_tenant_domain = settings.DEV_TENANT_DOMAIN
                request.tenant = Tenant.objects.get(domain=dev_tenant_domain)
            except Tenant.DoesNotExist:
                # If no tenant exists, check if any tenants are in the DB
                if not Tenant.objects.exists():
                    # Create a default tenant if none exist.
                    # This happens on the very first request after database setup.
                    request.tenant = Tenant.objects.create(
                        name="Default Tenant", domain=dev_tenant_domain
                    )
                else:
                    # If other tenants exist, but not the development one, it's an error.
                    raise NotFound(
                        detail=f"Development tenant for domain '{dev_tenant_domain}' not found."
                    )
        else:
            try:
                request.tenant = Tenant.objects.get(domain=hostname)
            except Tenant.DoesNotExist:
                raise NotFound(detail="Tenant not found for this domain.")

        # Set the RLS session variable
        if request.tenant:
            with connection.cursor() as cursor:
                cursor.execute("SET app.tenant_id = %s", [str(request.tenant.id)])

        response = self.get_response(request)

        with connection.cursor() as cursor:
            cursor.execute("RESET app.tenant_id")

        return response
