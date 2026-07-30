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

    def __init__(self, *args, service_area=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Server-side: narrow the service choices when the area is known
        # (used for query-param pre-selection and as a no-JS fallback).
        if service_area and service_area in Inquiry.SERVICE_AREA_MAP:
            allowed = Inquiry.SERVICE_AREA_MAP[service_area]
            self.fields['service'].choices = [
                (v, l) for v, l in Inquiry.SERVICE_CHOICES if v in allowed
            ]
        else:
            self.fields['service'].choices = list(Inquiry.SERVICE_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        service_area = cleaned_data.get('service_area')
        service = cleaned_data.get('service')

        if service_area and service_area in Inquiry.SERVICE_AREA_MAP:
            allowed = Inquiry.SERVICE_AREA_MAP[service_area]
            if service and service not in allowed:
                self.add_error(
                    'service',
                    'The selected service is not available under the chosen service area.'
                )

        return cleaned_data

    class Meta:
        model = Inquiry

        fields = [
            'full_name',
            'email',
            'phone_number',
            'organisation',
            'service_area',
            'service',
            'programme',
            'message'
        ]