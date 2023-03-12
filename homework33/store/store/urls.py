from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game_store.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('api.urls')),
    path('cart/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
