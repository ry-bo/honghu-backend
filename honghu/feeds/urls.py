from django.urls import path

from .views import HotPicsAPIView
app_name = 'feeds'

urlpatterns = [
    path('hot/', HotPicsAPIView.as_view(), name='hot'),
]
