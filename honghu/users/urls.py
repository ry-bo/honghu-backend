from django.urls import path

from .views import UserCreateViewSet
app_name = 'users'

urlpatterns = [
    path('mp/', UserCreateViewSet.as_view(), name='mp'),
]
