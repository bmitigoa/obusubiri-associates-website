from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

    # Service Pages
    path(
        'services/external-audit/',
        views.external_audit,
        name='external_audit'
    ),

    path(
        'services/tax-advisory/',
        views.tax_advisory,
        name='tax_advisory'
    ),

    path(
        'services/tax-objections-appeals/',
        views.tax_objections,
        name='tax_objections'
    ),

    path(
        'services/internal-audit/',
        views.internal_audit,
        name='internal_audit'
    ),

    path(
        'services/tax-return-filing/',
        views.tax_return_filing,
        name='tax_return_filing'
    ),

    path(
        'services/tax-exemption/',
        views.tax_exemption,
        name='tax_exemption'
    ),

    path(
        'services/accounting-bookkeeping/',
        views.accounting_bookkeeping,
        name='accounting_bookkeeping'
    ),

    path(
        'services/financial-advisory/',
        views.financial_advisory,
        name='financial_advisory'
    ),

    path(
    'services/project-audit/',
    views.project_audit,
    name='project_audit'
    ),

    path(
    'services/capacity-building/',
    views.capacity_building,
    name='capacity_building'
    ),

    # Blog
    path(
        'blog/kra-tax-objection-guide/',
        views.blog_kra_tax_objection,
        name='blog_kra_tax_objection'
    ),

    path(
    'blog/tax-appeals-tribunal-guide/',
    views.blog_tax_appeals,
    name='blog_tax_appeals'
   ),

   path(
    'blog/applying-for-tax-exemptions/',
    views.blog_tax_exemption,
    name='blog_tax_exemption'
  ),

    path('training/', views.training, name='training'),
    path('contact/', views.contact, name='contact'),
]