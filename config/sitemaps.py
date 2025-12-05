from django.contrib.sitemaps import Sitemap
from django.conf import settings

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set protocol based on DEBUG mode
        if not settings.DEBUG:
            self.protocol = 'https'
        else:
            self.protocol = 'http'

    def items(self):
        # Return URLs for both language versions
        return [
            '/',      # Arabic (default)
            '/en/',   # English
        ]

    def location(self, item):
        return item

