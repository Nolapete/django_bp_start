from rest_framework import serializers
from .models import CustomUser
from apps.tenants.serializers import TenantSerializer  # Import the TenantSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    """

    # Use the nested TenantSerializer for the tenant field
    tenant = TenantSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "tenant"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # The `password` is a write-only field, so we must handle it manually
        password = validated_data.pop("password", None)
        user = CustomUser.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user

    def validate(self, data):
        # Perform custom validation here to check for uniqueness within the tenant
        tenant = data.get("tenant")
        username = data.get("username")
        email = data.get("email")

        if tenant:
            if CustomUser.objects.filter(tenant=tenant, username=username).exists():
                raise serializers.ValidationError(
                    {
                        "username": "A user with this username already exists in this tenant."
                    }
                )
            if CustomUser.objects.filter(tenant=tenant, email=email).exists():
                raise serializers.ValidationError(
                    {"email": "A user with this email already exists in this tenant."}
                )

        return data
