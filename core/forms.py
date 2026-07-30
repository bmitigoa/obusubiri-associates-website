from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):

    programme = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
    )

    SERVICE_AREA_CHOICES = [
        ('', '— Select a service area —'),
        ('Audit & Assurance', 'Audit & Assurance'),
        ('Tax Advisory & Compliance', 'Tax Advisory & Compliance'),
        ('Tax Objections & Appeals', 'Tax Objections & Appeals'),
        ('Capacity Building & Training', 'Capacity Building & Training'),
    ]

    service_area = forms.ChoiceField(
        choices=SERVICE_AREA_CHOICES,
        required=False,
        label='Service Area',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = Inquiry

        fields = [
            'full_name',
            'email',
            'phone_number',
            'organisation',
            'service_area',
            'service',
            'message'
        ]