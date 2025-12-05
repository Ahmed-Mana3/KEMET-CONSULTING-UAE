from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.contrib.sitemaps.views import sitemap
from config.sitemaps import StaticViewSitemap

def robots_txt(request):
    content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /media/
Sitemap: https://kemetvision.com/sitemap.xml
"""
    return HttpResponse(content, content_type='text/plain')

# Sitemap configuration
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/setlang/', set_language, name='set_language'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
]

# Language-aware URL patterns
urlpatterns += i18n_patterns(
    path("", include("app.urls")),
    prefix_default_language=False,
)

# Serve media & static in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handlers
handler404 = 'app.views.page_not_found'
handler500 = 'app.views.server_error'