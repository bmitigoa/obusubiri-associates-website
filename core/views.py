from django.shortcuts import render
from django.core.mail import send_mail

from .forms import InquiryForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

def tax_objections(request):

    content = """
    <h2>Tax Objections & Appeals</h2>

    <p>
    We assist businesses, NGOs and institutions in challenging
    incorrect tax assessments issued by the Kenya Revenue Authority (KRA).
    </p>

    <p>
    Our team supports clients in preparing objections,
    compiling supporting documentation, responding to KRA,
    and representing clients before the Tax Appeals Tribunal.
    </p>

    <h3>Our Services Include:</h3>

    <ul>
        <li>Tax objection preparation</li>
        <li>Tax dispute resolution</li>
        <li>Appeals before the Tax Appeals Tribunal</li>
        <li>Tax compliance reviews</li>
    </ul>
    """

    return render(
        request,
        "service_detail.html",
        {
            "title": "Tax Objections & Appeals",
            "content": content
        }
    )


def tax_advisory(request):

    content = """
    <h2>Tax Advisory Services</h2>

    <p>
    We provide strategic tax planning and compliance advice
    to organisations across Kenya.
    </p>

    <ul>
        <li>Corporate tax planning</li>
        <li>VAT advisory</li>
        <li>PAYE compliance</li>
        <li>Tax risk assessments</li>
    </ul>
    """

    return render(
        request,
        "service_detail.html",
        {
            "title": "Tax Advisory Services",
            "content": content
        }
    )


def external_audit(request):

    content = """
    <h2>External Audit Services</h2>

    <p>
    Independent audit services that enhance transparency,
    accountability and stakeholder confidence.
    </p>

    <ul>
        <li>NGO audits</li>
        <li>Company audits</li>
        <li>Donor-funded project audits</li>
        <li>Statutory audits</li>
    </ul>
    """

    return render(
        request,
        "service_detail.html",
        {
            "title": "External Audit Services",
            "content": content
        }
    )


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