from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'organisation',
        'service_area',
        'service',
        'programme',
        'email',
        'created_at'
    )

    list_filter = ('service_area',)

    search_fields = (
        'full_name',
        'organisation',
        'email',
        'service_area'
    )