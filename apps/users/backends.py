from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from apps.tenants.models import Tenant


class TenantModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        tenant = request.tenant

        if tenant:
            try:
                user = UserModel.objects.get(username=username, tenant=tenant)
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist:
                return None
        return None
