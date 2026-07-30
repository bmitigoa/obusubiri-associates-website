from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):

    programme = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
    )

    class Meta:
        model = Inquiry

        fields = [
            'full_name',
            'email',
            'phone_number',
            'organisation',
            'service',
            'message'
        ]