# Import necessary modules and classes for testing
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from accounts.forms import *  # Import forms from the accounts app
from accounts.models import *  # Import models from the accounts app
from allauth.account.models import EmailAddress
from django.core.files.uploadedfile import SimpleUploadedFile


# Test cases for profile-related views
class ProfileViewTests(TestCase):

    def setUp(self):
        # Set up a test client
        self.client = Client()
        # Create a user and set up their profile
        self.user = User.objects.create_user(
            email='testuser@test.com',
            username="test",
            password='testpass',
            first_name='testy',
            last_name='testy'
        )
        # Create a user profile for the created user
        self.user_profile = UserProfile.objects.create(user=self.user)

        # Mark the email as verified to simulate a real user login with Allauth
        EmailAddress.objects.create(
            user=self.user,
            email='testuser@test.com',
            verified=True,
            primary=True
        )

        # Use the client to log in through Allauth's login view
        self.client.post(reverse('account_login'), {
            'login': 'testuser@test.com',
            'password': 'testpass'
        })

    # Test that the profile view renders correctly for logged-in users
    def test_profile_view(self):
        """Test the profile view renders correctly for logged-in users."""
        response = self.client.get(reverse('profile'))  # Get the profile page
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertTemplateUsed(response, 'accounts/profile.html')

        # Capture messages from the request
        messages = list(get_messages(response.wsgi_request))
        # Check if the welcome message is among them
        self.assertTrue(
            any("Welcome" in str(message) for message in messages),
            "The welcome message was not found in the response."
        )
        self.assertIn('profile', response.context)

    # Test that the user order history view
    # renders correctly for logged-in users
    def test_user_order_history_view(self):
        """Test the user order history view for logged-in users."""
        response = self.client.get(reverse('user_order_history'))
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertTemplateUsed(response, 'accounts/user_order_history.html')
        self.assertIn('order_history', response.context)

    # Test the GET request to the edit profile view
    def test_edit_profile_view_get(self):
        """Test the GET request to the edit profile view."""
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')
        self.assertIsInstance(response.context['form'], UserProfileForm)

    # Test submitting valid data to the edit profile view
    def test_edit_profile_view_post_valid(self):
        """Test submitting valid data to the edit profile view."""
        data = {
            'email': 'newemail@example.com',
            'phone_number': '1234567890',
            'address': '123 Main St',
            'date_of_birth': '1990-01-01',
            'current_weight': 75,
            'height': 180,
            'goal_weight': 70
        }
        response = self.client.post(reverse('edit_profile'), data, follow=True)
        self.assertEqual(response.status_code, 200)  # Check if response is OK

    # Test the GET request to add weight log view
    def test_add_weight_log_view_get(self):
        """Test the GET request to add weight log view."""
        response = self.client.get(reverse('add_weight_log'))
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertTemplateUsed(response, 'accounts/add_weight_log.html')
        self.assertIsInstance(response.context['form'], WeightLogForm)

    # Test submitting valid data to add weight log view
    def test_add_weight_log_view_post_valid(self):
        """Test submitting valid data to add weight log view."""
        data = {'weight': 75.5}  # Define valid weight data
        response = self.client.post(
            reverse('add_weight_log'), data, follow=True)
        self.assertRedirects(response, reverse('profile'))
        self.assertEqual(WeightLog.objects.filter(user=self.user).count(), 1)

    # Test retrieving user weight logs as JSON
    def test_get_user_weight_logs_view(self):
        """Test retrieving user weight logs as JSON."""
        WeightLog.objects.create(user=self.user, weight=75.5)
        response = self.client.get(reverse('get_user_weight_logs'))
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        weight_logs = response.json()  # Parse JSON response
        self.assertEqual(len(weight_logs), 1)  # Check if one log is returned
        self.assertIn('weight', weight_logs[0])

    # Test the GET request to edit weight log view
    def test_edit_weight_log_view_get(self):
        """Test the GET request to edit weight log view."""
        weight_log = WeightLog.objects.create(user=self.user, weight=75.5)
        response = self.client.get(
            reverse('edit_weight_log', args=[weight_log.id])
        )
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertTemplateUsed(response, 'accounts/edit_weight_log.html')
        self.assertIsInstance(response.context['form'], WeightLogForm)

    # Test submitting valid data to edit weight log view
    def test_edit_weight_log_view_post_valid(self):
        """Test submitting valid data to edit weight log view."""
        weight_log = WeightLog.objects.create(user=self.user, weight=75.5)
        data = {'weight': 76.0}  # Define new valid weight data
        response = self.client.post(
            reverse('edit_weight_log', args=[weight_log.id]), data, follow=True
        )
        self.assertRedirects(response, reverse('profile'))
        weight_log.refresh_from_db()
        self.assertEqual(weight_log.weight, 76.0)

    # Test deleting a weight log
    def test_delete_weight_log_view(self):
        """Test deleting a weight log."""
        weight_log = WeightLog.objects.create(user=self.user, weight=75.5)
        response = self.client.delete(
            reverse('delete-weight-log', args=[weight_log.id])
        )
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertFalse(WeightLog.objects.filter(id=weight_log.id).exists())

    # Test deleting the user profile
    def test_delete_user_profile_view(self):
        """Test deleting the user profile."""
        response = self.client.post(reverse('delete-user'), follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(User.objects.filter(username='testuser').exists())

    # Test submitting valid data to upload progress picture view
    def test_upload_progress_picture_view_post_valid(self):
        """Test submitting valid data to upload progress picture view."""
        # Create a sample valid image file
        progress_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=(
                b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00,'
                b'\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
            ),
            content_type='image/jpeg'
        )
        data = {'progress_image': progress_image}
        response = self.client.post(
            reverse('upload_progress_picture'), data, follow=True
        )
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertEqual(
            ProgressPicture.objects.filter(user=self.user_profile).count(), 1
        )
