from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


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

    wants_booking = models.BooleanField(
        default=False,
        verbose_name="This is a consultation booking request",
    )

    preferred_date = models.DateField(null=True, blank=True)

    TIME_SLOT_CHOICES = [
        ('', '— No preference —'),
        ('Morning (9:00 AM – 12:00 PM)', 'Morning (9:00 AM – 12:00 PM)'),
        ('Early Afternoon (12:00 PM – 2:00 PM)', 'Early Afternoon (12:00 PM – 2:00 PM)'),
        ('Late Afternoon (2:00 PM – 5:00 PM)', 'Late Afternoon (2:00 PM – 5:00 PM)'),
    ]
    preferred_time = models.CharField(
        max_length=60, choices=TIME_SLOT_CHOICES, blank=True, default='',
    )

    BOOKING_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('declined', 'Declined'),
    ]
    booking_status = models.CharField(
        max_length=20, choices=BOOKING_STATUS_CHOICES, default='pending', blank=True,
    )

    message = models.TextField()

    email_sent = models.BooleanField(
        default=True,
        help_text="False if the notification email failed to send.",
    )

    flagged_as_likely_spam = models.BooleanField(
        default=False,
        help_text="Automatically flagged because the message contained a "
                   "link. Not necessarily spam — please review before acting.",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.service_area and self.service:
            allowed = self.SERVICE_AREA_MAP.get(self.service_area, [])
            if self.service not in allowed:
                raise ValidationError(
                    {
                        'service': (
                            f"'{self.service}' is not available under "
                            f"'{self.service_area}'. "
                            f"Valid choices are: {', '.join(allowed) or 'none'}."
                        )
                    }
                )

        if self.wants_booking and not self.preferred_date:
            raise ValidationError(
                {
                    'preferred_date': (
                        "Please select a preferred date for your "
                        "consultation request."
                    )
                }
            )

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


class TeamMember(models.Model):
    """A staff profile shown in the 'Our Team' section of the About page."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Lower numbers appear first.",
    )
    active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this profile from the site without deleting it.",
    )

    class Meta:
        ordering = ['order', 'full_name']

    def __str__(self):
        return self.full_name

    @property
    def initials(self):
        letters = [part[0].upper() for part in self.full_name.split() if part]
        return ''.join(letters[:2]) or '?'


class Post(models.Model):
    """A self-service News & Insights article."""

    title = models.CharField(max_length=220)
    slug = models.SlugField(
        max_length=250, unique=True, blank=True,
        help_text="Leave blank to auto-generate from the title.",
    )
    excerpt = models.CharField(
        max_length=300, blank=True, default='',
        help_text="A short summary shown on the News list page. Leave "
                   "blank to auto-generate from the start of the article.",
    )
    body = models.TextField(
        help_text="Write the article in plain paragraphs. Leave a blank "
                   "line between paragraphs — no HTML or code needed.",
    )
    featured_image = models.ImageField(
        upload_to='news/', blank=True, null=True,
    )
    category = models.CharField(
        max_length=100, blank=True, default='',
        help_text="Optional, e.g. 'Tax Advisory'. Shown as a small label "
                   "on the article.",
    )
    is_published = models.BooleanField(
        default=True,
        help_text="Uncheck to save as a draft — it will not appear on "
                   "the website until this is checked.",
    )
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)[:250]
            slug = base_slug
            n = 2
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        if not self.excerpt and self.body:
            self.excerpt = self.body.strip()[:280]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title