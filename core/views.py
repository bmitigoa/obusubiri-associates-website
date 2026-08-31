import json
import logging

from django.shortcuts import render
from django.core.mail import send_mail

from .forms import InquiryForm

logger = logging.getLogger(__name__)


def home(request):
    sp_panels = [
        {
            'number': '01',
            'title': 'Audit & Assurance',
            'image': 'images/sp-audit.jpg',
            'image_alt': 'Audit team reviewing financial statements',
            'desc': (
                'Independent, evidence-based examination of financial records '
                'that builds stakeholder confidence and strengthens governance.'
            ),
            'items': [
                'External / statutory audits',
                'Internal audit services',
                'Donor-funded project audits',
                'Compliance & regulatory audits',
                'Fraud prevention reviews',
                'Risk & control assessments',
            ],
            'cta_text': 'Explore Audit Services',
            'cta_url': '/services/',
        },
        {
            'number': '02',
            'title': 'Tax Advisory & Compliance',
            'image': 'images/sp-tax.jpg',
            'image_alt': 'Tax documents and professional calculator on a desk',
            'desc': (
                'Strategic tax planning, accurate filing and expert representation '
                'to keep your organisation fully compliant and financially efficient.'
            ),
            'items': [
                'Corporate tax planning',
                'VAT & PAYE advisory',
                'Tax return filing',
                'Tax objections & KRA disputes',
                'Tax Appeals Tribunal support',
                'Tax exemption applications',
            ],
            'cta_text': 'Explore Tax Services',
            'cta_url': '/services/',
        },
        {
            'number': '03',
            'title': 'Financial Advisory',
            'image': 'images/sp-advisory.jpg',
            'image_alt': 'Professional advisory meeting in a modern boardroom',
            'desc': (
                'Practical financial guidance that improves performance, '
                'supports long-term planning and drives organisational sustainability.'
            ),
            'items': [
                'Strategic financial planning',
                'Budget development & review',
                'Cash flow management',
                'Accounting & bookkeeping',
                'Management accounts',
                'Performance analysis',
            ],
            'cta_text': 'Explore Advisory Services',
            'cta_url': '/services/',
        },
        {
            'number': '04',
            'title': 'Training & Capacity Building',
            'image': 'images/sp-capacity.jpg',
            'image_alt': 'Capacity building workshop session in East Africa',
            'desc': (
                'Tailored training programmes that strengthen institutional knowledge, '
                'improve compliance and build lasting staff capability.'
            ),
            'items': [
                'Board governance training',
                'Finance for non-finance managers',
                'Tax compliance workshops',
                'Internal control training',
                'Risk management training',
                'NGO financial management',
            ],
            'cta_text': 'Explore Training',
            'cta_url': '/training/',
        },
    ]
    return render(request, 'home.html', {
        'sp_id': 'home-services',
        'sp_label': 'What We Do',
        'sp_heading': 'Professional Services Built for Every Organisation',
        'sp_intro': (
            'From independent audits to strategic tax planning, advisory and '
            'capacity building — we deliver rigorous, practical expertise to '
            'NGOs, government bodies, SACCOs and private sector clients across '
            'Kenya and the wider region.'
        ),
        'sp_alt_bg': False,
        'sp_flip': False,
        'sp_badge_label': 'Our Services',
        'sp_panels': sp_panels,
    })


def about(request):
    sp_panels = [
        {
            'number': '01',
            'title': 'Audit & Assurance',
            'image': 'images/sp-audit.jpg',
            'image_alt': 'Audit team reviewing financial statements',
            'desc': (
                'Independent, evidence-based examination of financial records '
                'that builds stakeholder confidence and strengthens governance.'
            ),
            'items': [
                'External / statutory audits',
                'Internal audit services',
                'Donor-funded project audits',
                'Compliance & regulatory audits',
                'Fraud prevention reviews',
                'Risk & control assessments',
            ],
            'cta_text': 'Enquire about Audit & Assurance',
            'cta_url': '/contact/?service_area=Audit+%26+Assurance',
        },
        {
            'number': '02',
            'title': 'Tax Advisory & Compliance',
            'image': 'images/sp-tax.jpg',
            'image_alt': 'Tax documents and professional calculator on a desk',
            'desc': (
                'Strategic tax planning, accurate filing and expert representation '
                'to keep your organisation fully compliant and financially efficient.'
            ),
            'items': [
                'Corporate tax planning',
                'VAT & PAYE advisory',
                'Tax return filing',
                'KRA objections & disputes',
                'Tax Appeals Tribunal support',
                'Tax exemption applications',
            ],
            'cta_text': 'Enquire about Tax Advisory',
            'cta_url': '/contact/?service_area=Tax+Advisory+%26+Compliance',
        },
        {
            'number': '03',
            'title': 'Tax Objections & Appeals',
            'image': 'images/sp-advisory.jpg',
            'image_alt': 'Professional advisor preparing a tax objection document',
            'desc': (
                'Expert representation at the Tax Appeals Tribunal and '
                'professionally prepared objections that protect your tax position.'
            ),
            'items': [
                'KRA tax objection preparation',
                'Dispute resolution support',
                'Tax Appeals Tribunal representation',
                'Assessment review & analysis',
                'Documentation & evidence packs',
                'Follow-up with authorities',
            ],
            'cta_text': 'Enquire about Tax Objections',
            'cta_url': '/contact/?service_area=Tax+Objections+%26+Appeals',
        },
        {
            'number': '04',
            'title': 'Capacity Building & Training',
            'image': 'images/sp-capacity.jpg',
            'image_alt': 'Capacity building workshop session in East Africa',
            'desc': (
                'Tailored training programmes that strengthen institutional knowledge, '
                'improve compliance and build lasting staff capability.'
            ),
            'items': [
                'Board governance training',
                'Finance for non-finance managers',
                'Tax compliance workshops',
                'Internal control training',
                'Risk management training',
                'NGO financial management',
            ],
            'cta_text': 'Enquire about Training',
            'cta_url': '/contact/?service_area=Capacity+Building+%26+Training',
        },
    ]
    return render(request, 'about.html', {
        'sp_id': 'about-expertise',
        'sp_label': 'Expertise',
        'sp_heading': 'Our Areas of Expertise',
        'sp_intro': (
            'Practical professional solutions that strengthen governance, '
            'compliance and organisational performance across East Africa.'
        ),
        'sp_alt_bg': False,
        'sp_flip': True,
        'sp_badge_label': 'Expertise',
        'sp_panels': sp_panels,
    })


def services(request):
    sp_panels = [
        {
            'number': '01',
            'title': 'Audit & Assurance',
            'image': 'images/sp-audit.jpg',
            'image_alt': 'Audit professionals reviewing financial statements',
            'desc': (
                'We conduct rigorous independent audits for organisations of all types — '
                'giving funders, boards and regulators the assurance they need.'
            ),
            'items': [
                'Statutory / external audits',
                'Internal audit engagements',
                'Donor-funded project audits',
                'Expenditure verification',
                'Grant compliance reviews',
                'Governance & fraud reviews',
            ],
            'cta_text': 'External Audit detail',
            'cta_url': '/services/external-audit/',
        },
        {
            'number': '02',
            'title': 'Tax Advisory & Compliance',
            'image': 'images/sp-tax.jpg',
            'image_alt': 'Tax documents, forms and calculator on a professional desk',
            'desc': (
                'Comprehensive tax services from strategic planning through to dispute '
                'resolution — helping your organisation stay compliant and tax-efficient.'
            ),
            'items': [
                'Corporate & individual tax planning',
                'VAT & PAYE compliance',
                'Annual tax return filing',
                'KRA tax objection preparation',
                'Tax Appeals Tribunal representation',
                'Tax exemption applications',
            ],
            'cta_text': 'Tax Advisory detail',
            'cta_url': '/services/tax-advisory/',
        },
        {
            'number': '03',
            'title': 'Financial Advisory & Accounting',
            'image': 'images/sp-advisory.jpg',
            'image_alt': 'Financial advisory meeting in a corporate boardroom',
            'desc': (
                'We partner with finance teams to sharpen financial management, '
                'improve reporting quality and support long-term strategic decisions.'
            ),
            'items': [
                'Strategic financial planning',
                'Budgeting & forecasting',
                'Cash flow analysis',
                'Bookkeeping & management accounts',
                'Financial statement preparation',
                'Payroll & statutory reporting',
            ],
            'cta_text': 'Financial Advisory detail',
            'cta_url': '/services/financial-advisory/',
        },
        {
            'number': '04',
            'title': 'Training & Capacity Building',
            'image': 'images/sp-capacity.jpg',
            'image_alt': 'Training workshop session with African professionals',
            'desc': (
                'Practical, organisation-specific training that equips boards, '
                'finance staff and teams with skills that stick.'
            ),
            'items': [
                'Board governance & oversight',
                'Finance for non-finance managers',
                'Tax compliance workshops',
                'Internal controls training',
                'Risk management frameworks',
                'NGO financial management',
            ],
            'cta_text': 'Training programmes',
            'cta_url': '/training/',
        },
    ]
    return render(request, 'services.html', {
        'sp_id': 'services-detail',
        'sp_label': 'Service Areas',
        'sp_heading': 'How We Help Your Organisation',
        'sp_intro': (
            'Each service area is delivered by experienced professionals '
            'with deep sector knowledge and a practical, client-first approach.'
        ),
        'sp_alt_bg': True,
        'sp_flip': True,
        'sp_badge_label': 'Service Areas',
        'sp_panels': sp_panels,
    })


# --------
# SERVICE PAGES
# --------

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

def project_audit(request):

    content = """
    <p>
    We provide independent project audit services for donor-funded,
    development and institutional projects to ensure accountability,
    transparency and compliance with funding requirements.
    </p>

    <h3>Our Services Include:</h3>

    <ul>
        <li>Donor-funded project audits</li>
        <li>Grant compliance reviews</li>
        <li>Project financial audits</li>
        <li>Expenditure verification</li>
        <li>Risk and control assessments</li>
    </ul>
    """

    return render(
        request,
        "service_detail.html",
        {
            "title": "Project Audit Services",
            "content": content
        }
    )


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

def capacity_building(request):

    content = """
    <p>
    We help organisations strengthen institutional capacity through
    practical training programmes tailored to governance, finance,
    taxation and compliance requirements.
    </p>

    <h3>Our Training Areas Include:</h3>

    <ul>
        <li>Board governance training</li>
        <li>Finance for non-finance managers</li>
        <li>Tax compliance workshops</li>
        <li>Internal control training</li>
        <li>Risk management training</li>
    </ul>
    """

    return render(
        request,
        "service_detail.html",
        {
            "title": "Training & Capacity Building",
            "content": content
        }
    )


def blog_kra_tax_objection(request):

    return render(
        request,
        "service_detail.html",
        {
            "title": "Understanding Tax Objections in Kenya",
            "content": """


<h2>What is a Tax Objection?</h2>

<p>
A tax objection is a formal process that allows taxpayers to challenge
a tax assessment issued by the Kenya Revenue Authority (KRA) when they
believe the assessment is incorrect.
</p>

<p>
Businesses, NGOs, institutions and individuals have a legal right
to dispute assessments that do not accurately reflect their tax position.
</p>

<h2>Common Reasons for Filing a Tax Objection</h2>

<ul>
<li>Incorrect tax computations</li>
<li>Disallowed business expenses</li>
<li>VAT disputes</li>
<li>PAYE assessments</li>
<li>Withholding tax disputes</li>
<li>Penalty and interest disputes</li>
</ul>

<h2>Steps in Filing a Tax Objection</h2>

<ol>
<li>Review the assessment notice carefully.</li>
<li>Gather supporting documentation.</li>
<li>Prepare a detailed objection statement.</li>
<li>Submit the objection through the iTax platform.</li>
<li>Respond promptly to any KRA requests for clarification.</li>
</ol>

<h2>Importance of Professional Guidance</h2>

<p>
Tax disputes can have significant financial implications for an
organisation. Proper documentation, strong technical arguments and
timely responses greatly improve the chances of a successful outcome.
</p>

<p>
Professional tax advisors help organisations analyse assessments,
prepare supporting evidence and communicate effectively with KRA.
</p>

<h2>How Obusubiri MM & Associates Can Help</h2>

<p>
Our tax specialists assist organisations in reviewing tax assessments,
preparing professional objections, compiling evidence and representing
clients during engagements with KRA.
</p>

<div class="alert alert-light border-start border-4 border-warning mt-4">
<strong>Need assistance?</strong>
Contact our team today for professional tax objection support.
</div>

"""
        }
    )


# --------
# BLOG PAGE
# --------

def blog_kra_tax_objection(request):

    return render(
        request,
        "service_detail.html",
        {
            "title": "Understanding Tax Objections in Kenya",
            "content": """


<h2>What is a Tax Objection?</h2>

<p>
A tax objection is a formal process that allows taxpayers to challenge
a tax assessment issued by the Kenya Revenue Authority (KRA) when they
believe the assessment is incorrect.
</p>

<p>
Businesses, NGOs, institutions and individuals have a legal right
to dispute assessments that do not accurately reflect their tax position.
</p>

<h2>Common Reasons for Filing a Tax Objection</h2>

<ul>
<li>Incorrect tax computations</li>
<li>Disallowed business expenses</li>
<li>VAT disputes</li>
<li>PAYE assessments</li>
<li>Withholding tax disputes</li>
<li>Penalty and interest disputes</li>
</ul>

<h2>Steps in Filing a Tax Objection</h2>

<ol>
<li>Review the assessment notice carefully.</li>
<li>Gather supporting documentation.</li>
<li>Prepare a detailed objection statement.</li>
<li>Submit the objection through the iTax platform.</li>
<li>Respond promptly to any KRA requests for clarification.</li>
</ol>

<h2>Importance of Professional Guidance</h2>

<p>
Tax disputes can have significant financial implications for an
organisation. Proper documentation, strong technical arguments and
timely responses greatly improve the chances of a successful outcome.
</p>

<p>
Professional tax advisors help organisations analyse assessments,
prepare supporting evidence and communicate effectively with KRA.
</p>

<h2>How Obusubiri MM & Associates Can Help</h2>

<p>
Our tax specialists assist organisations in reviewing tax assessments,
preparing professional objections, compiling evidence and representing
clients during engagements with KRA.
</p>

<div class="alert alert-light border-start border-4 border-warning mt-4">
<strong>Need assistance?</strong>
Contact our team today for professional tax objection support.
</div>

"""
        }
    )

def blog_tax_appeals(request):

    return render(
        request,
        "service_detail.html",
        {
            "title": "Tax Appeals Tribunal Guide",
            "content": """

<h2>Introduction</h2>

<p>
The Tax Appeals Tribunal (TAT) is an independent body established under Kenyan law to hear and determine tax disputes between taxpayers and the Kenya Revenue Authority (KRA).
</p>

<p>
The Tribunal provides taxpayers with an opportunity to challenge objection decisions issued by KRA through a structured and legally recognised process.
</p>

<h2>When Should a Taxpayer Appeal?</h2>

<p>
A taxpayer may file an appeal when they are dissatisfied with the objection decision issued by KRA after lodging a tax objection.
</p>

<p>
The appeal process allows taxpayers to present facts, evidence and legal arguments supporting their position before an independent Tribunal.
</p>

<h2>Documents Commonly Required</h2>

<ul>
<li>Notice of Appeal</li>
<li>Statement of Facts</li>
<li>Copy of KRA Assessment</li>
<li>Copy of Objection Decision</li>
<li>Supporting Financial Documentation</li>
<li>Relevant Tax Correspondence</li>
</ul>

<h2>Importance of Proper Preparation</h2>

<p>
Tax appeals often involve technical tax legislation, financial records and procedural requirements. Inadequate preparation may weaken a taxpayer's case and affect the outcome of the appeal.
</p>

<p>
Professional support helps ensure that submissions are properly documented, timelines are met and legal arguments are effectively presented.
</p>

<h2>Benefits of Professional Representation</h2>

<ul>
<li>Improved case preparation</li>
<li>Reduced procedural errors</li>
<li>Professional documentation</li>
<li>Strategic tax advice</li>
<li>Effective engagement with tax authorities</li>
</ul>

<h2>How Obusubiri MM & Associates Can Help</h2>

<p>
We assist businesses, NGOs and institutions in preparing appeal documentation, analysing tax assessments, compiling supporting evidence and navigating the Tax Appeals Tribunal process.
</p>

<p>
Our goal is to help clients pursue fair outcomes while maintaining compliance with applicable tax laws and regulations.
</p>

"""
        }
    )

def blog_tax_exemption(request):

    return render(
        request,
        "service_detail.html",
        {
            "title": "Applying for Tax Exemptions in Kenya",
            "content": """

<h2>Introduction</h2>

<p>
Tax exemptions provide qualifying organisations with an opportunity to reduce their tax obligations and direct more resources towards achieving their objectives.
</p>

<p>
In Kenya, certain organisations including NGOs, charitable institutions, religious organisations and public benefit entities may qualify for tax exemptions subject to approval by the Kenya Revenue Authority (KRA).
</p>

<h2>Who May Qualify for Tax Exemptions?</h2>

<p>
Eligibility for tax exemption depends on the nature of an organisation and the activities it undertakes.
</p>

<p>
Organisations that operate for charitable, educational, religious, humanitarian or public benefit purposes may qualify for consideration under applicable tax laws.
</p>

<h2>Documents Commonly Required</h2>

<ul>
<li>Certificate of Registration or Incorporation</li>
<li>Organisation Constitution or Governing Documents</li>
<li>Audited Financial Statements</li>
<li>Evidence of Charitable or Public Benefit Activities</li>
<li>Project Reports and Supporting Documentation</li>
<li>Compliance and Regulatory Documents</li>
</ul>

<h2>Importance of Proper Preparation</h2>

<p>
Applications for tax exemption require careful preparation and adequate supporting documentation.
</p>

<p>
Proper preparation helps demonstrate that an organisation satisfies the eligibility requirements and operates in accordance with applicable regulations.
</p>

<h2>Benefits of Tax Exemption</h2>

<ul>
<li>Reduced tax obligations</li>
<li>Improved financial sustainability</li>
<li>Increased resources for programme activities</li>
<li>Enhanced donor confidence</li>
<li>Strengthened regulatory compliance</li>
</ul>

<h2>How Obusubiri MM & Associates Can Help</h2>

<p>
We assist NGOs, charitable organisations, religious institutions and other qualifying entities throughout the tax exemption application process.
</p>

<p>
Our services include eligibility assessments, document reviews, application preparation, compliance evaluations and professional support during engagements with relevant authorities.
</p>

"""
        }
    )

def training(request):
    sp_panels = [
        {
            'number': '01',
            'title': 'Board Governance',
            'image': 'images/sp-capacity.jpg',
            'image_alt': 'Capacity building workshop session in East Africa',
            'desc': (
                'Equipping board members and senior leaders with the governance '
                'knowledge, tools and frameworks to fulfil their oversight '
                'responsibilities effectively.'
            ),
            'items': [
                'Roles and responsibilities of board members',
                'Board oversight and accountability',
                'Strategic planning for boards',
                'Board-management relations',
                'Governance best practices for NGOs and SACCOs',
                'Risk oversight and compliance',
            ],
            'cta_text': 'Request this Programme',
            'cta_url': '/contact/?programme=Board+Governance',
        },
        {
            'number': '02',
            'title': 'Finance for Non-Finance Managers',
            'image': 'images/sp-capacity.jpg',
            'image_alt': 'Capacity building workshop session in East Africa',
            'desc': (
                'Practical financial literacy training that enables programme '
                'managers, project officers and non-finance staff to read, '
                'interpret and use financial information confidently.'
            ),
            'items': [
                'Understanding financial statements',
                'Budget monitoring and variance analysis',
                'Internal controls and accountability',
                'Cash flow concepts for managers',
                'Donor reporting and compliance',
                'Cost management and value for money',
            ],
            'cta_text': 'Request this Programme',
            'cta_url': '/contact/?programme=Finance+for+Non-Finance+Managers',
        },
        {
            'number': '03',
            'title': 'Tax Compliance',
            'image': 'images/sp-capacity.jpg',
            'image_alt': 'Capacity building workshop session in East Africa',
            'desc': (
                'Hands-on workshops that build staff capacity to meet tax '
                'obligations accurately and on time — reducing risk and '
                'strengthening regulatory compliance across the organisation.'
            ),
            'items': [
                'Corporate tax obligations and filing',
                'VAT registration, returns and compliance',
                'PAYE and payroll tax management',
                'Withholding tax requirements',
                'Tax exemptions for NGOs and charities',
                'iTax platform and KRA engagement',
            ],
            'cta_text': 'Request this Programme',
            'cta_url': '/contact/?programme=Tax+Compliance',
        },
        {
            'number': '04',
            'title': 'Risk Management',
            'image': 'images/sp-capacity.jpg',
            'image_alt': 'Capacity building workshop session in East Africa',
            'desc': (
                'Structured training that helps organisations identify, assess '
                'and manage risks — building a culture of proactive risk '
                'awareness and resilient internal controls.'
            ),
            'items': [
                'Enterprise risk management frameworks',
                'Risk identification and assessment',
                'Risk registers and reporting',
                'Internal control design and review',
                'Fraud prevention and detection',
                'Business continuity planning',
            ],
            'cta_text': 'Request this Programme',
            'cta_url': '/contact/?programme=Risk+Management',
        },
    ]
    from .models import TrainingAudience
    who_we_train = TrainingAudience.objects.all()

    from website.models import TrainingIntro
    training_intro = TrainingIntro.get_solo()

    return render(request, 'training.html', {
        'training_intro': training_intro,
        'sp_id': 'training-programmes',
        'sp_label': 'Programme Topics',
        'sp_heading': 'Training Programmes That Build Lasting Capability',
        'sp_intro': (
            'Our programmes combine practical content, experienced facilitators '
            'and interactive delivery to give participants skills they can apply '
            'immediately within their organisations.'
        ),
        'sp_alt_bg': False,
        'sp_flip': False,
        'sp_badge_label': 'Training',
        'sp_panels': sp_panels,
        'who_we_train': who_we_train,
    })


def contact(request):

    from .models import Inquiry as _Inquiry
    service_area_map_json = json.dumps(_Inquiry.SERVICE_AREA_MAP)
    all_service_choices = _Inquiry.SERVICE_CHOICES

    if request.method == 'POST':

        form = InquiryForm(request.POST)

        if form.is_valid():

            if form.is_probably_spam():
                # Honeypot field was filled in: a real visitor cannot do
                # this. Show the same success screen so a bot has no way
                # to tell it was blocked, but skip saving and emailing.
                return render(
                    request,
                    'contact.html',
                    {
                        'form': InquiryForm(),
                        'success': True,
                        'email_sent': True,
                        'submitted_name': form.cleaned_data.get('full_name', ''),
                        'submitted_service': form.cleaned_data.get('service', ''),
                        'submitted_service_area': form.cleaned_data.get('service_area', ''),
                        'submitted_programme': form.cleaned_data.get('programme', ''),
                        'service_area_map_json': service_area_map_json,
                        'all_service_choices': all_service_choices,
                    }
                )

            inquiry = form.save()
            programme = form.cleaned_data.get('programme', '')
            service_area = form.cleaned_data.get('service_area', '')

            programme_line = f"\nProgramme Requested: {programme}" if programme else ""
            service_area_line = f"\nService Area: {service_area}" if service_area else ""

            try:
                send_mail(
                    subject=f"New Website Inquiry - {inquiry.service}",
                    message=f"""
New inquiry received from the website.

Name: {inquiry.full_name}
Email: {inquiry.email}
Phone: {inquiry.phone_number}
Organisation: {inquiry.organisation}
Service Required: {inquiry.service}{service_area_line}{programme_line}

Message:
{inquiry.message}
                    """,
                    from_email='info@obusubiriassociates.co.ke',
                    recipient_list=['info@obusubiriassociates.co.ke'],
                    fail_silently=False,
                )
            except Exception:
                logger.warning(
                    "Failed to send enquiry notification email for inquiry pk=%s",
                    inquiry.pk,
                    exc_info=True,
                )
                inquiry.email_sent = False
                inquiry.save(update_fields=['email_sent'])

            return render(
                request,
                'contact.html',
                {
                    'form': InquiryForm(),
                    'success': True,
                    'email_sent': inquiry.email_sent,
                    'submitted_name': form.cleaned_data.get('full_name', ''),
                    'submitted_service': form.cleaned_data.get('service', ''),
                    'submitted_service_area': service_area,
                    'submitted_programme': programme,
                    'service_area_map_json': service_area_map_json,
                    'all_service_choices': all_service_choices,
                }
            )

    else:
        programme = request.GET.get('programme', '')
        service_area = request.GET.get('service_area', '')
        initial = {}
        if programme:
            initial['service'] = 'Training & Capacity Building'
            initial['programme'] = programme
        if service_area:
            initial['service_area'] = service_area
        form = InquiryForm(initial=initial, service_area=service_area or None)

    return render(
        request,
        'contact.html',
        {
            'form': form,
            'service_area_map_json': service_area_map_json,
            'all_service_choices': all_service_choices,
        }
    )