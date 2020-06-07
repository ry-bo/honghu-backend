import requests
import logging
from rest_framework import serializers
from .models import User
from django.conf import settings

logger = logging.getLogger(__name__)


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['username'] = OpenidUtils(
            validated_data['username']).get_openid()
        user, created = User.objects.get_or_create(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'auth_token',
        )
        read_only_fields = ('auth_token', )


class OpenidUtils(object):
    def __init__(self, jscode):
        self.url = "https://api.weixin.qq.com/sns/jscode2session"
        self.appid = settings.MP_APPID
        self.secret = settings.MP_SECRET
        self.jscode = jscode  # 前端传回的动态jscode

    def get_openid(self):
        url = self.url + "?appid=" + self.appid + "&secret=" + self.secret + "&js_code=" + self.jscode + "&grant_type=authorization_code"
        r = requests.get(url)
        r_json = r.json()
        openid = r_json['openid']

        return openid
