from django.contrib import admin, sitemaps
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
#Import the two above for static file handling

from django.contrib.sitemaps.views import sitemap
from myblog.sitemaps import Post_Sitemap

sitemaps = {
    'post': Post_Sitemap(),
    #Any model that worked on will be called here
}

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("django-check-seo/", include("django_check_seo.urls")),
    path('', include('myblog.urls')),
    #The two below for django auth. systems with built in templates
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    #Below for sitemap.xml generation used for crawling
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('cms.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
