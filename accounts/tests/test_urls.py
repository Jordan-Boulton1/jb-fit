# Import necessary modules and classes for testing
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from allauth.account import views as allauth_views  # Import views from allauth
from accounts import views  # Import custom views from accounts app


# Test cases for URLs related to Django Allauth views
class AllauthURLTests(TestCase):
    # Test that the signup URL resolves to the correct Allauth view
    def test_signup_url_resolves(self):
        url = reverse('account_signup')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.SignupView
        )

    # Test that the login URL resolves to the correct Allauth view
    def test_login_url_resolves(self):
        url = reverse('account_login')  # Get URL for login
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.LoginView
        )

    # Test that the logout URL resolves to the correct Allauth view
    def test_logout_url_resolves(self):
        url = reverse('account_logout')  # Get URL for logout
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.LogoutView
        )

    # Test that the password reset URL resolves to the correct Allauth view
    def test_password_reset_url_resolves(self):
        url = reverse('account_reset_password')  # Get URL for password reset
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.PasswordResetView
        )

    # Test that the password reset done URL
    # resolves to the correct Allauth view
    def test_password_reset_done_url_resolves(self):
        url = reverse('account_reset_password_done')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.PasswordResetDoneView
        )

    # Test that the email verification sent URL
    # resolves to the correct Allauth view
    def test_email_verification_sent_url_resolves(self):
        url = reverse('account_email_verification_sent')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.EmailVerificationSentView
        )


# Test cases for custom URLs in the accounts app
class TestURLs(SimpleTestCase):
    # Test that various accounts URLs resolve to the correct views
    def test_accounts_urls(self):
        """Test that accounts URLs resolve correctly."""
        url = reverse('profile')  # Get URL for the profile view
        self.assertEqual(resolve(url).func, views.profile_view)

        url = reverse('user_order_history')  # Get URL for user order history
        self.assertEqual(resolve(url).func, views.user_order_history)

        url = reverse('edit_profile')  # Get URL for edit profile
        self.assertEqual(resolve(url).func, views.edit_profile_view)

        url = reverse('add_weight_log')  # Get URL for adding a weight log
        self.assertEqual(resolve(url).func, views.add_weight_log)

        url = reverse('upload_progress_picture')
        self.assertEqual(resolve(url).func, views.upload_progress_picture)

        url = reverse('get_user_weight_logs')
        self.assertEqual(resolve(url).func, views.get_user_weight_logs)

        url = reverse('get_user_weight_logs_history')
        self.assertEqual(resolve(url).func, views.get_user_weight_logs_history)
        url = reverse('delete-user')  # Get URL for deleting a user profile
        self.assertEqual(resolve(url).func, views.delete_user_profile)

    # Test dynamic URLs that require parameters
    def test_dynamic_urls(self):
        """Test dynamic URLs with parameters."""
        url = reverse('delete_progress_picture', args=[1])
        self.assertEqual(resolve(url).func, views.delete_progress_picture)

        url = reverse('edit_weight_log', args=[1])
        self.assertEqual(resolve(url).func, views.edit_weight_log)

        url = reverse('delete-weight-log', args=[1])
        self.assertEqual(resolve(url).func, views.delete_weight_log)
