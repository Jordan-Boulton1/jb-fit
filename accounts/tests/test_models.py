# Import necessary modules and classes for testing
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts.models import *  # Import all models from accounts app
from datetime import date


# Test cases for the UserProfile model
class TestUserProfileModel(TestCase):
    def setUp(self):
        # Set up a user and associated user profile for testing
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

    # Test that the UserProfile instance is created correctly
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

    # Test updating a UserProfile instance
    def test_user_profile_update(self):
        """
        Test updating a UserProfile instance.
        """
        self.user_profile.phone_number = "0987654321"  # Update phone number
        self.user_profile.save()  # Save changes
        updated_profile = UserProfile.objects.get(id=self.user_profile.id)
        self.assertEqual(updated_profile.phone_number, "0987654321")

    # Test deleting a UserProfile instance
    def test_user_profile_deletion(self):
        """
        Test deleting a UserProfile instance.
        """
        self.user_profile.delete()  # Delete the user profile
        with self.assertRaises(UserProfile.DoesNotExist):
            UserProfile.objects.get(id=self.user_profile.id)


# Test cases for the WeightLog model
class WeightLogModelTest(TestCase):
    def setUp(self):
        # Create a sample user for testing
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            username='testusername',
            password='correct_password'
        )

    # Test that a WeightLog instance can be created successfully
    def test_weightlog_creation(self):
        """Test that a WeightLog instance can be created successfully."""
        weight_log = WeightLog.objects.create(
            user=self.user,
            weight=70.50
        )
        self.assertIsInstance(weight_log, WeightLog)  # Check instance type
        self.assertEqual(weight_log.user, self.user)  # Check user association
        self.assertEqual(weight_log.weight, 70.50)  # Check weight value
        self.assertIsNotNone(weight_log.entry_date)  # Check entry date is set

    # Test the string representation of a WeightLog instance
    def test_str_representation(self):
        """Test the string representation of a WeightLog instance."""
        weight_log = WeightLog.objects.create(
            user=self.user,
            weight=70.50
        )
        expected_str = (
            f"{self.user.username} - {weight_log.weight} kg on "
            f"{weight_log.entry_date.strftime('%Y-%m-%d')}"
        )
        self.assertEqual(str(weight_log), expected_str)

    # Test that the weight field maintains the correct decimal precision
    def test_weight_decimal_precision(self):
        """Test that the weight field maintains
        the correct decimal precision."""
        weight_log = WeightLog.objects.create(
            user_id=self.user.id,  # Associate with user
            weight=70.555,  # Use weight with more than two decimal places
        )
        # Assert that the weight was saved with correct precision (rounded)
        self.assertEqual(weight_log.weight, Decimal('70.56'))


# Test cases for the ProgressPicture model
class ProgressPictureModelTest(TestCase):
    def setUp(self):
        # Create a sample user and associated user profile for testing
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            gender='Male',
            date_of_birth='1990-01-01'
        )

    # Test that a ProgressPicture instance can be created successfully
    def test_progresspicture_creation(self):
        """Test that a ProgressPicture instance can be created successfully."""
        progress_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=(
                b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00,'
                b'\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
            ),
            content_type='image/jpeg'
        )
        progress_picture = ProgressPicture.objects.create(
            user=self.user_profile,
            progress_image=progress_image
        )
        self.assertIsInstance(progress_picture, ProgressPicture)
        self.assertEqual(progress_picture.user, self.user_profile)
        self.assertIsNotNone(progress_picture.uploaded_at)

    # Test that a ProgressPicture instance can be created without an image
    def test_progresspicture_creation_without_image(self):
        """Test that a ProgressPicture instance
        can be created without an image."""
        progress_picture = ProgressPicture.objects.create(
            user=self.user_profile
        )
        self.assertIsInstance(progress_picture, ProgressPicture)
        self.assertEqual(progress_picture.user, self.user_profile)
        self.assertEqual(progress_picture.progress_image.name, None)
        self.assertIsNotNone(progress_picture.uploaded_at)

    # Test the string representation of a ProgressPicture instance
    def test_str_representation(self):
        """Test the string representation of a ProgressPicture instance."""
        progress_picture = ProgressPicture.objects.create(
            user=self.user_profile,
            progress_image=None
        )
        expected_str = f"{self.user.username} - {progress_picture.uploaded_at}"
        self.assertEqual(str(progress_picture), expected_str)
