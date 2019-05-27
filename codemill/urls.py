
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activity/', include('api.urls')),
    path('reward/', include('reward.urls')),
    path('achievement/', include('achievement.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

