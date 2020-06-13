from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('honghu.users.urls', namespace='users')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
