from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse

from website.sitemaps import ProjectSitemap, StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
}


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        "Sitemap: https://prengaconstruction.al/sitemap.xml\n"
    )
    return HttpResponse(content, content_type='text/plain')

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
