from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import UserProfile
from datetime import date

# Create your tests here.


class TestUserProfileModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            phone_number='1234567890',
            address='123 Test St, Test City, Test Country',
            gender='Male',
            date_of_birth=date(1990, 1, 1),
            current_weight=70.5,
            height=175.0,
            goal_weight=65.0
        )

    def test_user_profile_creation(self):
        """
        Test if the UserProfile instance is created correctly.
        """
        self.assertEqual(self.user_profile.user.username, 'testuser')
        self.assertEqual(self.user_profile.phone_number, "1234567890")
        self.assertEqual(
            self.user_profile.address,
            "123 Test St, Test City, Test Country"
        )
        self.assertEqual(self.user_profile.gender, "Male")
        self.assertEqual(self.user_profile.date_of_birth, date(1990, 1, 1))
        self.assertEqual(self.user_profile.current_weight, 70.5)
        self.assertEqual(self.user_profile.height, 175.0)
        self.assertEqual(self.user_profile.goal_weight, 65.0)

    def test_user_profile_str(self):
        """
        Test the __str__ method of the UserProfile model.
        """
        self.assertEqual(str(self.user_profile), self.user.username)

    def test_user_profile_update(self):
        """
        Test updating a UserProfile instance.
        """
        self.user_profile.phone_number = "0987654321"
        self.user_profile.save()
        updated_profile = UserProfile.objects.get(id=self.user_profile.id)
        self.assertEqual(updated_profile.phone_number, "0987654321")

    def test_user_profile_deletion(self):
        """
        Test deleting a UserProfile instance.
        """
        self.user_profile.delete()
        with self.assertRaises(UserProfile.DoesNotExist):
            UserProfile.objects.get(id=self.user_profile.id)
