from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):

    programme = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
    )

    # Honeypot spam trap: a real visitor never sees or fills this field (it
    # is hidden with CSS, not just the "hidden" input type, and skipped in
    # tab order). Simple bots that auto-fill every input on the page tend to
    # fill it anyway, which the view uses to silently discard the submission
    # in InquiryForm.is_probably_spam() below.
    website = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'tabindex': '-1',
            'class': 'hp-field',
            'aria-hidden': 'true',
        }),
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

    def is_probably_spam(self):
        """True if the honeypot field was filled in, which a real visitor
        cannot do since it is invisible and unreachable by tab. Call this
        after the form has been validated (is_valid() / clean())."""
        return bool(self.cleaned_data.get('website'))

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
            'message',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+254 700 000 000',
            }),
            'organisation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your organisation',
            }),
            'service': forms.Select(attrs={
                'class': 'form-select',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Briefly describe what you need help with…',
            }),
        }