from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import HttpResponse

def robots_txt(request):
    content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /media/
Sitemap: https://kemetvision.com/sitemap.xml
"""
    return HttpResponse(content, content_type='text/plain')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    path('robots.txt', robots_txt),
]

# Serve media & static in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handlers
handler404 = 'app.views.page_not_found'
handler500 = 'app.views.server_error'