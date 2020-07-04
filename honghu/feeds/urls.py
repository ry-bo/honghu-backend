from django.urls import path

from .views import HotPicsAPIView
app_name = 'feeds'

urlpatterns = [
    path('new', HotPicsAPIView.as_view(), name='new'),
    path('recomend', HotPicsAPIView.as_view(), name='recomend'),
    path('hot', HotPicsAPIView.as_view(), name='hot'),
]
