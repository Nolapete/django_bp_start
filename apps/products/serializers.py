from rest_framework import serializers
from .models import Product
from apps.tenants.serializers import TenantSerializer


class ProductSerializer(serializers.ModelSerializer):
    # Use the nested TenantSerializer. Set as read_only.
    tenant = TenantSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "created_by", "tenant"]
