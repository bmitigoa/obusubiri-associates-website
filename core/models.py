from django.db import models


class Inquiry(models.Model):

    SERVICE_CHOICES = [
        ('External Audit', 'External Audit'),
        ('Internal Audit', 'Internal Audit'),
        ('Project Audit', 'Project Audit'),
        ('Tax Advisory', 'Tax Advisory'),
        ('Tax Return Filing', 'Tax Return Filing'),
        ('Accounting Services', 'Accounting Services'),
        ('Financial Advisory', 'Financial Advisory'),
        ('Training & Capacity Building', 'Training & Capacity Building'),
    ]

    # Maps each service area to the subset of SERVICE_CHOICES that belong to it.
    SERVICE_AREA_MAP = {
        'Audit & Assurance': [
            'External Audit',
            'Internal Audit',
            'Project Audit',
        ],
        'Tax Advisory & Compliance': [
            'Tax Advisory',
            'Tax Return Filing',
            'Accounting Services',
            'Financial Advisory',
        ],
        'Tax Objections & Appeals': [
            'Tax Advisory',
            'Financial Advisory',
        ],
        'Capacity Building & Training': [
            'Training & Capacity Building',
        ],
    }

    full_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone_number = models.CharField(max_length=50)

    organisation = models.CharField(max_length=200)

    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    SERVICE_AREA_CHOICES = [
        ('Audit & Assurance', 'Audit & Assurance'),
        ('Tax Advisory & Compliance', 'Tax Advisory & Compliance'),
        ('Tax Objections & Appeals', 'Tax Objections & Appeals'),
        ('Capacity Building & Training', 'Capacity Building & Training'),
    ]

    service_area = models.CharField(
        max_length=100,
        choices=SERVICE_AREA_CHOICES,
        blank=True,
        default='',
    )

    programme = models.CharField(max_length=200, blank=True, default='')

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class TrainingAudience(models.Model):
    """Represents a single 'Who We Train' tile on the training page."""

    icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class, e.g. 'bi bi-people-fill'",
    )
    label = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Lower numbers appear first.",
    )

    class Meta:
        ordering = ['order', 'label']
        verbose_name = 'Training Audience'
        verbose_name_plural = 'Training Audiences'

    def __str__(self):
        return self.label