from django.test import TestCase
from contact.models import ContactSubmission


class ContactSubmissionModelTest(TestCase):

    def test_contact_submission_creation(self):
        submission = ContactSubmission.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            message='This is a test message.'
        )

        self.assertEqual(str(submission), 'John Doe - john.doe@example.com')
        self.assertEqual(submission.first_name, 'John')
        self.assertEqual(submission.last_name, 'Doe')
        self.assertEqual(submission.email, 'john.doe@example.com')
        self.assertEqual(submission.message, 'This is a test message.')
