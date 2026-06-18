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

    full_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone_number = models.CharField(max_length=50)

    organisation = models.CharField(max_length=200)

    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name