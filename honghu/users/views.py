from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CreateUserSerializer


class UserCreateViewSet(generics.CreateAPIView):
    """
    Creates user accounts
    """
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
