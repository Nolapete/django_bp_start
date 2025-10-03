from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing CustomUser instances.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
