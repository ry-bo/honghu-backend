from django.urls import path

from .views import HotPicsAPIView, PicDetailAPIView, RecommandPicsAPIView, NewPicsAPIView
app_name = 'feeds'

urlpatterns = [
    path('new', HotPicsAPIView.as_view(), name='new'),
    path('recommend', RecommandPicsAPIView.as_view(), name='recommend'),
    path('hot', NewPicsAPIView.as_view(), name='hot'),
    path('detail/<int:pk>/', PicDetailAPIView.as_view(), name='detail'),
]
