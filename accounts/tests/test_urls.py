from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from allauth.account import views as allauth_views
from accounts import views


class AllauthURLTests(TestCase):
    def test_signup_url_resolves(self):
        url = reverse('account_signup')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.SignupView
        )

    def test_login_url_resolves(self):
        url = reverse('account_login')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.LoginView
        )

    def test_logout_url_resolves(self):
        url = reverse('account_logout')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.LogoutView
        )

    def test_password_reset_url_resolves(self):
        url = reverse('account_reset_password')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.PasswordResetView
        )

    def test_password_reset_done_url_resolves(self):
        url = reverse('account_reset_password_done')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.PasswordResetDoneView
        )

    def test_email_verification_sent_url_resolves(self):
        url = reverse('account_email_verification_sent')
        self.assertEqual(
            resolve(url).func.view_class,
            allauth_views.EmailVerificationSentView
        )


class TestURLs(SimpleTestCase):
    def test_accounts_urls(self):
        """Test that accounts URLs resolve correctly."""
        url = reverse('profile')
        self.assertEqual(resolve(url).func, views.profile_view)

        url = reverse('user_order_history')
        self.assertEqual(resolve(url).func, views.user_order_history)

        url = reverse('edit_profile')
        self.assertEqual(resolve(url).func, views.edit_profile_view)

        url = reverse('add_weight_log')
        self.assertEqual(resolve(url).func, views.add_weight_log)

        url = reverse('upload_progress_picture')
        self.assertEqual(resolve(url).func, views.upload_progress_picture)

        url = reverse('get_user_weight_logs')
        self.assertEqual(resolve(url).func, views.get_user_weight_logs)

        url = reverse('get_user_weight_logs_history')
        self.assertEqual(resolve(url).func, views.get_user_weight_logs_history)

        url = reverse('delete-user')
        self.assertEqual(resolve(url).func, views.delete_user_profile)

    def test_dynamic_urls(self):
        """Test dynamic URLs with parameters."""
        url = reverse('delete_progress_picture', args=[1])
        self.assertEqual(resolve(url).func, views.delete_progress_picture)

        url = reverse('edit_weight_log', args=[1])
        self.assertEqual(resolve(url).func, views.edit_weight_log)

        url = reverse('delete-weight-log', args=[1])
        self.assertEqual(resolve(url).func, views.delete_weight_log)
