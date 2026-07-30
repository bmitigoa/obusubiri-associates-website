from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'organisation',
        'service',
        'programme',
        'email',
        'created_at'
    )

    search_fields = (
        'full_name',
        'organisation',
        'email'
    )