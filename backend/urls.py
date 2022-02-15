

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from lib import views
from django.conf.urls import url

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('lib.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('lib.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
