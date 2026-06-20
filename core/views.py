from django.shortcuts import render
from django.core.mail import send_mail

from .forms import InquiryForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def training(request):
    return render(request, 'training.html')


def contact(request):

    if request.method == 'POST':

        form = InquiryForm(request.POST)

        if form.is_valid():

            inquiry = form.save()

            send_mail(
                subject=f"New Website Inquiry - {inquiry.service}",
                message=f"""
New inquiry received from the website.

Name: {inquiry.full_name}
Email: {inquiry.email}
Phone: {inquiry.phone_number}
Organisation: {inquiry.organisation}
Service Required: {inquiry.service}

Message:
{inquiry.message}
                """,
                from_email='info@obusubiriassociates.co.ke',
                recipient_list=['info@obusubiriassociates.co.ke'],
                fail_silently=False,
            )

            return render(
                request,
                'contact.html',
                {
                    'form': InquiryForm(),
                    'success': True
                }
            )

    else:

        form = InquiryForm()

    return render(
        request,
        'contact.html',
        {
            'form': form
        }
    )