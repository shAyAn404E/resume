"""
URL configuration for HShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from django.contrib.sitemaps.views import sitemap
from store.sitemaps import ProductSitemap


sitemaps_dict = {
    'products': ProductSitemap,
}


urlpatterns = [
    path('Dadasham/', admin.site.urls),
    path('',include('store.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="sitemap"),
]

handler401 = 'store.views.custom_401_view'
handler403 = 'store.views.custom_403_view'
handler404 = 'store.views.custom_404_view'
handler500 = 'store.views.custom_500_view'

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


