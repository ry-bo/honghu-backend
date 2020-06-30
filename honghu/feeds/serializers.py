from rest_framework import serializers
from photologue.models import Photo

class HotPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'