import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Inquiry, TrainingAudience

_FORMULA_PREFIXES = ('=', '+', '-', '@', '\t', '\r')


def _safe_csv_value(value):
    """Prevent CSV formula injection by prefixing dangerous cell values."""
    if value is None:
        return ''
    text = str(value)
    if text.lstrip() and text.lstrip()[0] in _FORMULA_PREFIXES:
        return "'" + text
    return text


def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inquiries.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'full_name', 'email', 'phone_number', 'organisation',
        'service_area', 'service', 'programme', 'message', 'created_at',
    ])

    for inquiry in queryset:
        writer.writerow([
            _safe_csv_value(inquiry.full_name),
            _safe_csv_value(inquiry.email),
            _safe_csv_value(inquiry.phone_number),
            _safe_csv_value(inquiry.organisation),
            _safe_csv_value(inquiry.service_area),
            _safe_csv_value(inquiry.service),
            _safe_csv_value(inquiry.programme),
            _safe_csv_value(inquiry.message),
            inquiry.created_at,
        ])

    return response


export_as_csv.short_description = 'Export selected as CSV'


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'organisation',
        'service_area',
        'service',
        'programme',
        'email',
        'email_sent',
        'created_at',
    )

    date_hierarchy = 'created_at'

    list_filter = ('service_area', 'service', 'programme', 'email_sent')

    search_fields = (
        'full_name',
        'organisation',
        'email',
        'service_area'
    )

    actions = [export_as_csv]


@admin.register(TrainingAudience)
class TrainingAudienceAdmin(admin.ModelAdmin):

    list_display = ('label', 'icon', 'order')
    list_editable = ('order',)
    ordering = ('order', 'label')

    class Media:
        js = ('js/admin-sortable.js',)