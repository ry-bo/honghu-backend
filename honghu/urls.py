from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('honghu.users.urls', namespace='users')),
    path('api/feeds/', include('honghu.feeds.urls', namespace='feeds')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
