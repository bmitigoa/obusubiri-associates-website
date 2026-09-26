import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Inquiry, Post, TeamMember, TrainingAudience

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
        'wants_booking', 'preferred_date', 'preferred_time', 'booking_status',
        'flagged_as_likely_spam',
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
            _safe_csv_value(inquiry.wants_booking),
            _safe_csv_value(inquiry.preferred_date),
            _safe_csv_value(inquiry.preferred_time),
            _safe_csv_value(inquiry.booking_status),
            _safe_csv_value(inquiry.flagged_as_likely_spam),
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
        'wants_booking',
        'preferred_date',
        'preferred_time',
        'booking_status',
        'flagged_as_likely_spam',
    )

    list_display_links = ('full_name',)

    list_editable = ('booking_status',)

    date_hierarchy = 'created_at'

    list_filter = ('service_area', 'service', 'programme', 'email_sent', 'wants_booking', 'booking_status', 'flagged_as_likely_spam')

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
    ordering = ('order', 'label')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'title', 'active', 'order')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return not TeamMember.objects.filter(user=request.user).exists()

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        return ('user',)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'is_published', 'published_at')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'excerpt', 'body')
    date_hierarchy = 'published_at'
    prepopulated_fields = {'slug': ('title',)}