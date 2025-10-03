from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer


class SensitiveEndpointAnonRateThrottle(AnonRateThrottle):
    rate = "3/minute"


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing CustomUser instances.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Handles user registration with per-tenant separation.
        """
        self.throttle_classes = [SensitiveEndpointAnonRateThrottle]

        # Pass the tenant from the request context to the serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        """
        Performs the create operation, setting the tenant for the new user.
        """
        serializer.save(tenant=self.request.tenant)
