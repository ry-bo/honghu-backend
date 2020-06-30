from photologue.models import Photo
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import HotPicsSerializer


class HotPicsAPIView(generics.ListAPIView):
    ''''''
    queryset = Photo.objects.all()
    serializer_class = HotPicsSerializer
    permission_classes = [AllowAny, ]
