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
        Overrides the create method to apply throttling for registration.
        """
        self.throttle_classes = [SensitiveEndpointAnonRateThrottle]
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
