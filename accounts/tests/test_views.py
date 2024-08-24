from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages import get_messages
from accounts.models import UserProfile, WeightLog, ProgressPicture

class AccountsViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = UserProfile.objects.create(user=self.user)
        self.client.login(username='testuser', password='12345')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')
        self.assertEqual(response.context['profile'], self.profile)

    def test_edit_profile_view_get(self):
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')
        self.assertIn('form', response.context)

    def test_edit_profile_view_post(self):
        response = self.client.post(reverse('edit_profile'), {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName',
            'form_type': 'editProfile'
        })
        self.assertRedirects(response, reverse('profile'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'NewFirstName')
        self.assertEqual(self.user.last_name, 'NewLastName')

    def test_add_weight_log(self):
        response = self.client.post(reverse('add_weight_log'), {
            'weight': 70
        })
        self.assertRedirects(response, reverse('profile'))
        self.assertTrue(WeightLog.objects.filter(user=self.user, weight=70).exists())

    def test_get_user_weight_logs(self):
        WeightLog.objects.create(user=self.user, weight=70, entry_date=timezone.now())
        response = self.client.get(reverse('get_user_weight_logs'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_get_user_weight_logs_history(self):
        WeightLog.objects.create(user=self.user, weight=70, entry_date=timezone.now())
        response = self.client.get(reverse('get_user_weight_logs_history'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_edit_weight_log(self):
        weight_log = WeightLog.objects.create(user=self.user, weight=70, entry_date=timezone.now())
        response = self.client.post(reverse('edit_weight_log', args=[weight_log.id]), {
            'weight': 75
        })
        self.assertRedirects(response, reverse('profile'))
        weight_log.refresh_from_db()
        self.assertEqual(weight_log.weight, 75)

    def test_delete_weight_log(self):
        weight_log = WeightLog.objects.create(user=self.user, weight=70, entry_date=timezone.now())
        response = self.client.delete(reverse('delete-weight-log', args=[weight_log.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(WeightLog.objects.filter(id=weight_log.id).exists())

    def test_delete_user_profile(self):
        response = self.client.post(reverse('delete-user'))
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_upload_progress_picture(self):
        with open('path_to_image.jpg', 'rb') as img:
            response = self.client.post(reverse('upload_progress_picture'), {
                'image': SimpleUploadedFile(img.name, img.read(), content_type='image/jpeg')
            })
        self.assertRedirects(response, reverse('profile'))
        self.assertTrue(ProgressPicture.objects.filter(user=self.profile).exists())