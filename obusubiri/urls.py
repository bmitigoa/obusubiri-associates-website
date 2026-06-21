from django.contrib import admin
from django.urls import path, include
from core import views

from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    path('services/external-audit/', views.external_audit, name='external_audit'),
    path('services/tax-advisory/', views.tax_advisory, name='tax_advisory'),
    path('services/tax-objections-appeals/', views.tax_objections, name='tax_objections'),

]