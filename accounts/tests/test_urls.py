from django.test import TestCase
from django.urls import reverse, resolve
from allauth.account import views as allauth_views

class AllauthURLTests(TestCase):

    def test_signup_url_resolves(self):
        url = reverse('account_signup')
        self.assertEqual(resolve(url).func.view_class, allauth_views.SignupView)

    def test_login_url_resolves(self):
        url = reverse('account_login')
        self.assertEqual(resolve(url).func.view_class, allauth_views.LoginView)

    def test_logout_url_resolves(self):
        url = reverse('account_logout')
        self.assertEqual(resolve(url).func.view_class, allauth_views.LogoutView)

    def test_password_reset_url_resolves(self):
        url = reverse('account_reset_password')
        self.assertEqual(resolve(url).func.view_class, allauth_views.PasswordResetView)

    def test_password_reset_done_url_resolves(self):
        url = reverse('account_reset_password_done')
        self.assertEqual(resolve(url).func.view_class, allauth_views.PasswordResetDoneView)

    def test_email_verification_sent_url_resolves(self):
        url = reverse('account_email_verification_sent')
        self.assertEqual(resolve(url).func.view_class, allauth_views.EmailVerificationSentView)
