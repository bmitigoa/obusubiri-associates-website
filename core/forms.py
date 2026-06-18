from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):

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