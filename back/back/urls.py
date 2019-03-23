from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('game.urls')),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('profiles.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]
