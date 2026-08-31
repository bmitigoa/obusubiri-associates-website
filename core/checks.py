from django.core.checks import Error, register

from .models import Inquiry


@register()
def check_service_area_map_covers_all_services(app_configs, **kwargs):
    """
    Verify that every value in Inquiry.SERVICE_CHOICES appears in at least
    one Inquiry.SERVICE_AREA_MAP entry.

    If a developer adds a new service to SERVICE_CHOICES without also adding
    it to SERVICE_AREA_MAP, that service silently disappears from the contact
    form for visitors who have a service area pre-selected.
    """
    errors = []

    all_mapped_services = {
        service
        for services in Inquiry.SERVICE_AREA_MAP.values()
        for service in services
    }

    for value, _label in Inquiry.SERVICE_CHOICES:
        if value not in all_mapped_services:
            errors.append(
                Error(
                    f"Service '{value}' is in Inquiry.SERVICE_CHOICES but is not "
                    f"listed under any key in Inquiry.SERVICE_AREA_MAP.",
                    hint=(
                        "Add this service to at least one entry in "
                        "Inquiry.SERVICE_AREA_MAP in core/models.py."
                    ),
                    obj=Inquiry,
                    id='core.E001',
                )
            )

    return errors
