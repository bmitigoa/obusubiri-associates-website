from django.shortcuts import render
from django.core.mail import send_mail

from .forms import InquiryForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


# =========================
# SERVICE PAGES
# =========================

def external_audit(request):
    content = """
    <p>We provide professional external audit services for companies, NGOs, SACCOs and donor-funded projects.</p>

    <h3>Our Services Include:</h3>

    <ul>
        <li>Statutory audits</li>
        <li>NGO audits</li>
        <li>Donor-funded project audits</li>
        <li>Financial statement audits</li>
        <li>Compliance audits</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "External Audit Services",
        "content": content
    })


def tax_advisory(request):
    content = """
    <p>We provide strategic tax planning and compliance advice to organisations across Kenya.</p>

    <ul>
        <li>Corporate tax planning</li>
        <li>VAT advisory</li>
        <li>PAYE compliance reviews</li>
        <li>Tax risk assessments</li>
        <li>Tax compliance support</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "Tax Advisory Services",
        "content": content
    })


def tax_objections(request):
    content = """
    <p>We assist businesses, NGOs and institutions in challenging incorrect tax assessments issued by KRA.</p>

    <ul>
        <li>Tax objection preparation</li>
        <li>Tax dispute resolution</li>
        <li>Appeals before the Tax Appeals Tribunal</li>
        <li>Tax compliance reviews</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "Tax Objections & Appeals",
        "content": content
    })


def internal_audit(request):
    content = """
    <p>Our internal audit services help organisations improve operational efficiency, strengthen controls and manage risks.</p>

    <ul>
        <li>Risk assessments</li>
        <li>Internal control reviews</li>
        <li>Governance audits</li>
        <li>Fraud prevention reviews</li>
        <li>Process improvement recommendations</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "Internal Audit Services",
        "content": content
    })


def tax_return_filing(request):
    content = """
    <p>We assist organisations and individuals with preparing and filing tax returns accurately and on time.</p>

    <ul>
        <li>Corporate tax returns</li>
        <li>VAT returns</li>
        <li>PAYE returns</li>
        <li>Withholding tax returns</li>
        <li>Tax compliance reviews</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "Tax Return Filing Services",
        "content": content
    })


def tax_exemption(request):
    content = """
    <p>We guide NGOs, charities and qualifying organisations through tax exemption application procedures.</p>

    <ul>
        <li>Tax exemption applications</li>
        <li>KRA documentation support</li>
        <li>Application reviews</li>
        <li>Compliance assessments</li>
        <li>Follow-up with authorities</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "Tax Exemption Applications",
        "content": content
    })


def accounting_bookkeeping(request):
    content = """
    <p>We provide bookkeeping and accounting services that help organisations maintain accurate financial records.</p>

    <ul>
        <li>Bookkeeping services</li>
        <li>Financial statement preparation</li>
        <li>Payroll support</li>
        <li>Management accounts</li>
        <li>Monthly reporting</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "Accounting & Bookkeeping Services",
        "content": content
    })


def financial_advisory(request):
    content = """
    <p>We offer financial advisory services designed to improve financial performance and long-term sustainability.</p>

    <ul>
        <li>Financial planning</li>
        <li>Budget development</li>
        <li>Cash flow management</li>
        <li>Business performance analysis</li>
        <li>Strategic financial advice</li>
    </ul>
    """
    return render(request, "service_detail.html", {
        "title": "Financial Advisory Services",
        "content": content
    })


def blog_kra_tax_objection(request):
    content = """
    <p>If you disagree with a tax assessment issued by KRA, you have a legal right to lodge a tax objection.</p>

    <p>The objection must be submitted within the timelines provided by tax legislation and supported with relevant documentation.</p>

    <p>Professional guidance can significantly improve the quality of your objection and increase the chances of a successful outcome.</p>
    """
    return render(request, "service_detail.html", {
        "title": "How to File a Tax Objection with KRA in Kenya",
        "content": content
    })



# =========================
# BLOG PAGE
# =========================

def blog_kra_tax_objection(request):
    return render(
        request,
        "service_detail.html",
        {
            "title": "How to File a Tax Objection with KRA in Kenya",
            "subtitle": "A practical guide for businesses and organisations.",
            "content": """
            <p>
            If you disagree with a tax assessment issued by KRA,
            you have a legal right to lodge a tax objection.
            </p>

            <p>
            The objection must be submitted within the timelines
            provided by tax legislation and supported with relevant
            documentation.
            </p>

            <p>
            Professional guidance can significantly improve the quality
            of your objection and increase the chances of a successful outcome.
            </p>
            """
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