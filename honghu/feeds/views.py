from rest_framework import generics
from rest_framework.permissions import AllowAny
from photologue.models import Photo


from .serializers import PicsSerializer, PicSerializer


class NewPicsAPIView(generics.ListAPIView):
    '''新图速递'''
    queryset = Photo.objects.filter(is_public=True).all()
    serializer_class = PicsSerializer
    permission_classes = [
        AllowAny,
    ]


class RecommandPicsAPIView(generics.ListAPIView):
    ''''''
    queryset = Photo.objects.filter(is_public=True).order_by('?')[:100]
    serializer_class = PicsSerializer
    permission_classes = [
        AllowAny,
    ]


class HotPicsAPIView(generics.ListAPIView):
    ''''''
    queryset = Photo.objects.filter(is_public=True).order_by('-view_count')
    serializer_class = PicsSerializer
    permission_classes = [
        AllowAny,
    ]


class PicDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PicSerializer
    queryset = Photo.objects.all()
    permission_classes = [
        AllowAny,
    ]

    def get_object(self):
        object = super().get_object()
        object.increment_count()
        return object
