from django.contrib.sitemaps import Sitemap
from .models import Product

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.filter(is_active=True)  # یا همه‌ی محصولات

    def location(self, item):
        return f"/product/{item.id}/"  # اگر slug داری: return f"/product/{item.slug}/"
