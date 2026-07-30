import csv
import io
from unittest.mock import patch

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.core import mail

from .admin import export_as_csv, _safe_csv_value
from .models import Inquiry


class ContactFormProgrammeTests(TestCase):
    """Tests for the training programme enquiry flow on the contact page."""

    BASE_POST = {
        'full_name': 'Jane Doe',
        'email': 'jane@example.com',
        'phone_number': '+254712000000',
        'organisation': 'Test Org',
        'service': 'Training & Capacity Building',
        'service_area': 'Capacity Building & Training',
        'message': 'I am interested in this programme.',
    }

    def test_programme_name_appears_in_outbound_email(self):
        """Submitting the form with a programme value must include that
        programme name in the notification email sent to the team."""
        data = {**self.BASE_POST, 'programme': 'Board Governance'}
        self.client.post(reverse('contact'), data)

        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Board Governance', mail.outbox[0].body)
        self.assertIn('Programme Requested:', mail.outbox[0].body)

    def test_no_programme_line_in_email_when_programme_absent(self):
        """When no programme is submitted the email must NOT contain the
        'Programme Requested:' line."""
        data = {**self.BASE_POST, 'programme': ''}
        self.client.post(reverse('contact'), data)

        self.assertEqual(len(mail.outbox), 1)
        self.assertNotIn('Programme Requested:', mail.outbox[0].body)

    def test_service_preselected_as_training_when_programme_param_present(self):
        """A GET request with ?programme= must pre-fill the service field with
        'Training & Capacity Building'."""
        response = self.client.get(
            reverse('contact'), {'programme': 'Finance for Non-Finance Managers'}
        )
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertEqual(
            form.initial.get('service'),
            'Training & Capacity Building',
        )

    def test_programme_banner_rendered_when_programme_param_set(self):
        """The programme info banner must appear in the rendered HTML when the
        ?programme= query parameter is supplied."""
        response = self.client.get(
            reverse('contact'), {'programme': 'Risk Management'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Risk Management')
        self.assertContains(response, 'training programme')

    def test_programme_banner_absent_when_no_programme_param(self):
        """No programme banner should appear when ?programme= is not in the
        query string."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'training programme')

    def test_mail_failure_still_returns_success_page(self):
        """If the mail backend raises an exception the view must still return
        the success page — the inquiry is already saved to the database."""
        with patch('core.views.send_mail', side_effect=Exception('SMTP unavailable')):
            response = self.client.post(reverse('contact'), self.BASE_POST)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['success'])


class EnquirySummaryContextTests(TestCase):
    """Tests that the success context echoes back the submitted form values."""

    TRAINING_POST = {
        'full_name': 'Alice Kamau',
        'email': 'alice@example.com',
        'phone_number': '+254700111222',
        'organisation': 'Kenya NGO',
        'service': 'Training & Capacity Building',
        'service_area': 'Capacity Building & Training',
        'programme': 'Board Governance',
        'message': 'Please register me for the programme.',
    }

    NON_TRAINING_POST = {
        'full_name': 'Bob Otieno',
        'email': 'bob@example.com',
        'phone_number': '+254700333444',
        'organisation': 'Nairobi SACCO',
        'service': 'External Audit',
        'service_area': 'Audit & Assurance',
        'programme': '',
        'message': 'We need an external audit.',
    }

    def test_training_submission_context_contains_all_summary_fields(self):
        """A training enquiry (with programme) must echo name, service,
        service area and programme in the success context."""
        response = self.client.post(reverse('contact'), self.TRAINING_POST)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['success'])
        self.assertEqual(response.context['submitted_name'], 'Alice Kamau')
        self.assertEqual(
            response.context['submitted_service'], 'Training & Capacity Building'
        )
        self.assertEqual(
            response.context['submitted_service_area'], 'Capacity Building & Training'
        )
        self.assertEqual(response.context['submitted_programme'], 'Board Governance')

    def test_non_training_submission_context_contains_expected_fields(self):
        """A non-training enquiry (without programme) must echo name, service
        and service area; programme must be empty."""
        response = self.client.post(reverse('contact'), self.NON_TRAINING_POST)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['success'])
        self.assertEqual(response.context['submitted_name'], 'Bob Otieno')
        self.assertEqual(response.context['submitted_service'], 'External Audit')
        self.assertEqual(
            response.context['submitted_service_area'], 'Audit & Assurance'
        )

    def test_programme_is_empty_when_not_submitted(self):
        """submitted_programme must be an empty string when no programme is
        included in the POST — ensures the programme row is omitted from the
        confirmation page."""
        response = self.client.post(reverse('contact'), self.NON_TRAINING_POST)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['success'])
        self.assertEqual(response.context['submitted_programme'], '')


class ExportInquiriesCSVTests(TestCase):
    """Tests for the export_as_csv admin action."""

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username='admin', password='password', email='admin@example.com'
        )
        self.factory = RequestFactory()
        self.inquiry = Inquiry.objects.create(
            full_name='Jane Doe',
            email='jane@example.com',
            phone_number='+254712000000',
            organisation='Test Org',
            service_area='Capacity Building & Training',
            service='Training & Capacity Building',
            programme='Board Governance',
            message='Hello world',
        )

    def _run_export(self, queryset=None):
        if queryset is None:
            queryset = Inquiry.objects.all()
        request = self.factory.get('/')
        request.user = self.superuser
        from .admin import InquiryAdmin
        ma = InquiryAdmin(Inquiry, AdminSite())
        return export_as_csv(ma, request, queryset)

    def test_response_content_type_and_disposition(self):
        response = self._run_export()
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertIn('attachment', response['Content-Disposition'])
        self.assertIn('inquiries.csv', response['Content-Disposition'])

    def test_header_row_contains_all_required_fields(self):
        response = self._run_export()
        content = response.content.decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        headers = next(reader)
        expected = [
            'full_name', 'email', 'phone_number', 'organisation',
            'service_area', 'service', 'programme', 'message', 'created_at',
        ]
        self.assertEqual(headers, expected)

    def test_data_row_contains_inquiry_values(self):
        response = self._run_export()
        content = response.content.decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        next(reader)  # skip header
        row = next(reader)
        self.assertEqual(row[0], 'Jane Doe')
        self.assertEqual(row[1], 'jane@example.com')
        self.assertEqual(row[4], 'Capacity Building & Training')
        self.assertEqual(row[6], 'Board Governance')

    def test_formula_injection_values_are_escaped(self):
        """Cell values beginning with formula characters must be prefixed with
        an apostrophe so spreadsheet software treats them as literal text."""
        Inquiry.objects.all().delete()
        Inquiry.objects.create(
            full_name='=CMD|"/C calc"!A0',
            email='safe@example.com',
            phone_number='+1234567890',
            organisation='+EvilOrg',
            service_area='-Area',
            service='@Service',
            programme='Normal',
            message='=SUM(1+1)',
        )
        response = self._run_export()
        content = response.content.decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        next(reader)  # skip header
        row = next(reader)
        # Each formula-prefixed value must start with apostrophe
        self.assertTrue(row[0].startswith("'"), f"full_name not escaped: {row[0]}")
        self.assertTrue(row[3].startswith("'"), f"organisation not escaped: {row[3]}")
        self.assertTrue(row[4].startswith("'"), f"service_area not escaped: {row[4]}")
        self.assertTrue(row[5].startswith("'"), f"service not escaped: {row[5]}")
        self.assertTrue(row[7].startswith("'"), f"message not escaped: {row[7]}")
        # Safe value must not be modified
        self.assertEqual(row[1], 'safe@example.com')
        self.assertEqual(row[6], 'Normal')


class ServiceAreaMapConsistencyTests(TestCase):
    """System-check level tests: SERVICE_AREA_MAP must cover every SERVICE_CHOICES value."""

    def test_every_service_choice_is_in_service_area_map(self):
        """Every value in SERVICE_CHOICES must appear in at least one SERVICE_AREA_MAP entry.

        Failing here means a service would silently disappear from the contact
        form for visitors who have a service area pre-selected.
        """
        all_mapped_services = {
            service
            for services in Inquiry.SERVICE_AREA_MAP.values()
            for service in services
        }
        missing = [
            value
            for value, _label in Inquiry.SERVICE_CHOICES
            if value not in all_mapped_services
        ]
        self.assertEqual(
            missing,
            [],
            msg=(
                f"The following SERVICE_CHOICES values are not listed in any "
                f"SERVICE_AREA_MAP entry: {missing}. Add them to at least one "
                f"area in Inquiry.SERVICE_AREA_MAP."
            ),
        )

    def test_service_area_map_contains_no_unknown_services(self):
        """Every service listed inside SERVICE_AREA_MAP must be a valid SERVICE_CHOICES value.

        Stale or misspelled entries in SERVICE_AREA_MAP would never be shown to
        users but indicate a data-integrity problem worth catching early.
        """
        valid_services = {value for value, _label in Inquiry.SERVICE_CHOICES}
        unknown = [
            service
            for services in Inquiry.SERVICE_AREA_MAP.values()
            for service in services
            if service not in valid_services
        ]
        self.assertEqual(
            unknown,
            [],
            msg=(
                f"SERVICE_AREA_MAP references services not in SERVICE_CHOICES: "
                f"{unknown}. Remove or correct these entries."
            ),
        )


class WhoWeTrainTileIntegrityTests(TestCase):
    """Sanity-check every 'Who We Train' tile in the training view."""

    def _get_who_we_train(self):
        from core.views import training
        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/training/')
        response = training(request)
        # Pull the list directly from the view context
        response = self.client.get(reverse('training'))
        return response.context['who_we_train']

    def test_every_tile_has_non_empty_icon(self):
        """Each tile must carry a non-empty icon string (Bootstrap Icons class)."""
        tiles = self._get_who_we_train()
        for tile in tiles:
            self.assertTrue(
                tile.icon.strip(),
                msg=f"Tile '{tile.label}' has a missing or blank icon.",
            )

    def test_every_tile_has_non_empty_label(self):
        """Each tile must carry a non-empty label string."""
        tiles = self._get_who_we_train()
        for tile in tiles:
            self.assertTrue(
                tile.label.strip(),
                msg="A tile has a missing or blank label.",
            )

    def test_every_tile_has_non_empty_desc(self):
        """Each tile must carry a non-empty description string."""
        tiles = self._get_who_we_train()
        for tile in tiles:
            self.assertTrue(
                tile.description.strip(),
                msg=f"Tile '{tile.label}' has a missing or blank description.",
            )


class SafeCSVValueTests(TestCase):
    """Unit tests for the _safe_csv_value helper."""

    def test_equals_prefix_is_escaped(self):
        self.assertEqual(_safe_csv_value('=1+1'), "'=1+1")

    def test_plus_prefix_is_escaped(self):
        self.assertEqual(_safe_csv_value('+1'), "'+1")

    def test_minus_prefix_is_escaped(self):
        self.assertEqual(_safe_csv_value('-1'), "'-1")

    def test_at_prefix_is_escaped(self):
        self.assertEqual(_safe_csv_value('@user'), "'@user")

    def test_leading_whitespace_then_formula_is_escaped(self):
        self.assertEqual(_safe_csv_value('  =formula'), "'  =formula")

    def test_normal_value_unchanged(self):
        self.assertEqual(_safe_csv_value('Jane Doe'), 'Jane Doe')

    def test_none_returns_empty_string(self):
        self.assertEqual(_safe_csv_value(None), '')

    def test_empty_string_unchanged(self):
        self.assertEqual(_safe_csv_value(''), '')
