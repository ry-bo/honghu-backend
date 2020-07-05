from rest_framework import serializers
from photologue.models import Photo


class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        exclude = [
            'sites',
        ]


class PicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id', 'image', 'title', 'view_count', 'crop_from', 'date_added'
        ]
