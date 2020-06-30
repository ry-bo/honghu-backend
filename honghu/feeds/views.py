from rest_framework import generics
from photologue.models import Photo
from .serializers import HotPicsSerializer


class HotPicsAPIView(generics.ListAPIView):
    ''''''
    queryset = Photo.objects.all()
    serializer_class = HotPicsSerializer
