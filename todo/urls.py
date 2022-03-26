from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from .yasg import urlpatterns as yasg_pat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('apps.todos.urls')),
    path('users/', include('apps.users.urls')),
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += yasg_pat

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
