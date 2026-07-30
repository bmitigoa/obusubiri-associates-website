from django.test import TestCase
from django.urls import reverse
from django.core import mail


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
