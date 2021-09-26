from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
#Import the two above for static file handling

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls')),
    #The two below for django auth. systems with built in templates
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)