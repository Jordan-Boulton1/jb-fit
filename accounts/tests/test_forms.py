# Import necessary modules and classes for testing
from django.test import TestCase
from unittest.mock import MagicMock
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date, timedelta
from accounts.forms import *  # Import custom forms from accounts app
from django.contrib.auth.models import User
from accounts.models import UserProfile


# Test cases for the CustomSignupForm
class CustomSignupFormTests(TestCase):
    def setUp(self):
        # Define valid data for form testing
        self.valid_data = {
            'email': 'testuser@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'gender': 'M',
            'date_of_birth': date(1990, 1, 1),
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
        }

    # Test that the form is valid with correct data
    def test_form_valid_data(self):
        form = CustomSignupForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    # Test that the form is invalid when first name is missing
    def test_form_missing_first_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data['first_name'] = ''
        form = CustomSignupForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertEqual(
            form.errors['first_name'],
            ['This field is required.']
        )

    # Test that the form is invalid when first name
    # contains non-alphabetical characters
    def test_form_invalid_first_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data['first_name'] = 'John123'
        form = CustomSignupForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertEqual(
            form.errors['first_name'],
            ['First name can only contain alphabetical characters.']
        )

    # Test that the form is invalid when last name is missing
    def test_form_missing_last_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data['last_name'] = ''
        form = CustomSignupForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)
        self.assertEqual(
            form.errors['last_name'],
            ['This field is required.']
        )

    # Test that the form is invalid when last name
    # contains non-alphabetical characters
    def test_form_invalid_last_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data['last_name'] = 'Doe123'
        form = CustomSignupForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)
        self.assertEqual(
            form.errors['last_name'],
            ['Last name can only contain alphabetical characters.']
        )

    # Test that the form is invalid if date of birth is in the future
    def test_form_date_of_birth_in_future(self):
        invalid_data = self.valid_data.copy()
        invalid_data['date_of_birth'] = date.today() + timedelta(days=1)
        form = CustomSignupForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)
        self.assertEqual(
            form.errors['date_of_birth'],
            ['Date of birth cannot be in the future.']
        )

    # Test that the form is invalid if passwords do not match
    def test_form_passwords_do_not_match(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'DifferentPass123!'
        form = CustomSignupForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
        self.assertEqual(
            form.errors['password2'],
            ['You must type the same password each time.']
        )

    # Test that the form saves correctly and creates a user and profile
    def test_form_save_creates_user_and_profile(self):
        form = CustomSignupForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

        # Mock request object
        mock_request = MagicMock()

        # Pass the mock request object to the form's save method
        user = form.save(request=mock_request)

        # Check user creation
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'testuser@example.com')

        # Check profile creation
        user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(user_profile.gender, 'Male')
        self.assertEqual(user_profile.date_of_birth, date(1990, 1, 1))

    # Test form save when user profile already exists
    def test_form_save_existing_user_profile(self):
        user = User.objects.create(
            username='testuser',
            email='testuser@example.com'
        )
        UserProfile.objects.create(user=user)

        form = CustomSignupForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

        # Mock request object
        mock_request = MagicMock()

        user = form.save(request=mock_request)

        # Check profile update
        user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(user_profile.gender, 'Male')
        self.assertEqual(user_profile.date_of_birth, date(1990, 1, 1))


# Test cases for the CustomLoginForm
class CustomLoginFormTest(TestCase):
    def setUp(self):
        # Sample valid data for the form
        self.valid_data = {
            'login': 'testuser@example.com',
            'password': 'correct_password',
        }

        # Create a user with the valid data
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            username='testusername',
            password='correct_password'
        )

    # Test form initialization and check for correct widget attributes
    def test_form_initialization(self):
        """Test that form fields have the correct widget attributes."""
        form = CustomLoginForm()
        self.assertEqual(
            form.fields['login'].widget.attrs['class'], 'form-control'
        )
        self.assertEqual(
            form.fields['login'].widget.attrs['placeholder'], 'Email address'
        )
        self.assertEqual(
            form.fields['password'].widget.attrs['class'], 'form-control'
        )
        self.assertEqual(
            form.fields['password'].widget.attrs['placeholder'], 'Password'
        )
        # Remember field class check
        self.assertEqual(
            form.fields['remember'].widget.attrs['class'], 'form-check-input'
        )

    # Test form validation with valid data
    def test_form_valid_data(self):
        """Test form validation with valid data."""
        form = CustomLoginForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    # Test form validation with an invalid email format
    def test_form_invalid_email(self):
        """Test form validation with an invalid email format."""
        invalid_data = self.valid_data.copy()
        invalid_data['login'] = 'invalid-email'  # Invalid email
        form = CustomLoginForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('login', form.errors)
        self.assertEqual(
            form.errors['login'],
            ['Enter a valid email address.']
        )

    # Test form validation with missing password
    def test_form_missing_password(self):
        """Test form validation with missing password."""
        invalid_data = self.valid_data.copy()
        invalid_data.pop('password')  # Remove password
        form = CustomLoginForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertEqual(
            form.errors['password'],
            ['This field is required.']
        )

    # Test form validation with completely empty data
    def test_form_empty_data(self):
        """Test form validation with completely empty data."""
        form = CustomLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('login', form.errors)
        self.assertIn('password', form.errors)
        self.assertEqual(form.errors['login'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])


# Test cases for the UserProfileForm
class UserProfileFormTest(TestCase):
    def setUp(self):
        # Create a test user and user profile
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            phone_number='1234567890',
            address='123 Test St',
            date_of_birth=date(1990, 1, 1),
            current_weight=70.5,
            height=175.0,
            goal_weight=65.0
        )
        # Define valid data for form testing
        self.valid_data = {
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'address': '123 Test St',
            'date_of_birth': '1990-01-01',
            'current_weight': 70.5,
            'height': 175.0,
            'goal_weight': 65.0,
            'image': None,
        }

    # Test that the form initializes with correct initial data
    def test_form_initialization(self):
        """Test that the form initializes with correct initial data."""
        form = UserProfileForm(instance=self.profile)
        self.assertEqual(form.fields['email'].initial, self.user.email)
        self.assertEqual(form.fields['date_of_birth'].initial, '1990-01-01')

    # Test that form fields have the correct attributes
    def test_form_field_attributes(self):
        """Test that form fields have the correct attributes."""
        form = UserProfileForm()
        self.assertEqual(
            form.fields['email'].widget.attrs['class'], 'form-control'
        )
        self.assertEqual(
            form.fields['image'].widget.attrs['class'], 'form-control'
        )
        self.assertEqual(
            form.fields['date_of_birth'].widget.attrs['class'], 'form-control'
        )

    # Test that the form is valid with correct data
    def test_form_valid_data(self):
        """Test that the form is valid with correct data."""
        form = UserProfileForm(data=self.valid_data, instance=self.profile)
        self.assertTrue(form.is_valid())

    # Test that the form is invalid if required fields are missing
    def test_form_missing_required_fields(self):
        """Test that the form is invalid if required fields are missing."""
        required_fields = [
            'email', 'phone_number', 'address', 'date_of_birth',
            'current_weight', 'height', 'goal_weight'
        ]
        for field in required_fields:
            invalid_data = self.valid_data.copy()
            invalid_data.pop(field)
            form = UserProfileForm(data=invalid_data, instance=self.profile)
            self.assertFalse(form.is_valid())
            self.assertIn(field, form.errors)

    # Test that form validation fails for invalid email
    def test_invalid_email(self):
        """Test that form validation fails for invalid email."""
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'invalid-email'
        form = UserProfileForm(data=invalid_data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    # Test that form validation fails if the email already exists
    def test_duplicate_email(self):
        """Test that form validation fails if the email already exists."""
        another_user = User.objects.create_user(
            username='anotheruser',
            email='another@example.com',
            password='password123'
        )
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'another@example.com'
        form = UserProfileForm(data=invalid_data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(
            form.errors['email'], ['This email address is already in use.']
        )

    # Test that form validation fails for non-digit phone numbers
    def test_invalid_phone_number(self):
        """Test that form validation fails for non-digit phone numbers."""
        invalid_data = self.valid_data.copy()
        invalid_data['phone_number'] = 'invalid-phone'
        form = UserProfileForm(data=invalid_data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
        self.assertEqual(
            form.errors['phone_number'],
            ['Phone number must contain only digits.']
        )

    # Test that form validation fails for non-positive current weight
    def test_invalid_current_weight(self):
        """Test that form validation fails for non-positive current weight."""
        invalid_data = self.valid_data.copy()
        invalid_data['current_weight'] = -1
        form = UserProfileForm(data=invalid_data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('current_weight', form.errors)
        self.assertEqual(
            form.errors['current_weight'],
            ['Current weight must be greater than zero.']
        )

    # Test that form validation fails for non-positive height
    def test_invalid_height(self):
        """Test that form validation fails for non-positive height."""
        invalid_data = self.valid_data.copy()
        invalid_data['height'] = 0
        form = UserProfileForm(data=invalid_data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('height', form.errors)
        self.assertEqual(
            form.errors['height'],
            ['Height must be greater than zero.']
        )

    # Test that form validation fails for non-positive goal weight
    def test_invalid_goal_weight(self):
        """Test that form validation fails for non-positive goal weight."""
        invalid_data = self.valid_data.copy()
        invalid_data['goal_weight'] = -5
        form = UserProfileForm(data=invalid_data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('goal_weight', form.errors)
        self.assertEqual(
            form.errors['goal_weight'],
            ['Goal weight must be greater than zero.']
        )

    # Test that form validation fails if date of birth is in the future
    def test_future_date_of_birth(self):
        """Test that form validation fails
        if date of birth is in the future."""
        invalid_data = self.valid_data.copy()
        invalid_data['date_of_birth'] = (
            (datetime.today().date() + timedelta(days=1)).isoformat()
        )
        form = UserProfileForm(data=invalid_data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)
        self.assertEqual(
            form.errors['date_of_birth'],
            ['Date of birth cannot be in the future.']
        )

    # Test that form save updates the user and profile correctly
    def test_form_save(self):
        """Test that form save updates the user and profile correctly."""
        form = UserProfileForm(data=self.valid_data, instance=self.profile)
        self.assertTrue(form.is_valid())
        profile = form.save()
        self.assertEqual(profile.user.email, 'testuser@example.com')
        self.assertEqual(profile.phone_number, '1234567890')
        self.assertEqual(profile.current_weight, 70.5)
        self.assertEqual(profile.height, 175.0)


# Test cases for the WeightLogForm
class WeightLogFormTest(TestCase):
    def setUp(self):
        # Sample valid and invalid data for the form
        self.valid_data = {'weight': 70.5}
        self.invalid_data_negative_weight = {'weight': -5}
        self.invalid_data_zero_weight = {'weight': 0}

    # Test that the form initializes with correct field attributes
    def test_form_initialization(self):
        """Test that the form initializes with correct field attributes."""
        form = WeightLogForm()
        self.assertEqual(
            form.fields['weight'].widget.attrs.get('class'), 'form-control'
        )
        self.assertEqual(
            form.fields['weight'].widget.attrs.get('step'), '0.1'
        )

    # Test that the form is valid with correct data
    def test_form_valid_data(self):
        """Test that the form is valid with correct data."""
        form = WeightLogForm(data=self.valid_data)
        self.assertTrue(
            form.is_valid(),
            f"Expected form to be valid with data: {self.valid_data}"
        )

    # Test that the form is invalid if required fields are missing
    def test_form_missing_required_field(self):
        """Test that the form is invalid if required fields are missing."""
        form = WeightLogForm(data={})  # Missing weight field
        self.assertFalse(form.is_valid())
        self.assertIn('weight', form.errors)
        self.assertEqual(form.errors['weight'], ['This field is required.'])

    # Test that the form accepts valid positive weight
    def test_clean_weight_positive(self):
        """Test that the form accepts valid positive weight."""
        form = WeightLogForm(data=self.valid_data)
        self.assertTrue(
            form.is_valid(), "Form should be valid with positive weight"
        )

    # Test that the form validation fails for negative weight
    def test_clean_weight_negative(self):
        """Test that the form validation fails for negative weight."""
        form = WeightLogForm(data=self.invalid_data_negative_weight)
        self.assertFalse(form.is_valid())
        self.assertIn('weight', form.errors)
        self.assertEqual(
            form.errors['weight'], ['Value must be greater than zero.']
        )

    # Test that the form validation fails for zero weight
    def test_clean_weight_zero(self):
        """Test that the form validation fails for zero weight."""
        form = WeightLogForm(data=self.invalid_data_zero_weight)
        self.assertFalse(form.is_valid())
        self.assertIn('weight', form.errors)
        self.assertEqual(
            form.errors['weight'], ['Value must be greater than zero.']
        )


# Test cases for the ProgressPictureForm
class ProgressPictureFormTest(TestCase):
    def setUp(self):
        # Create a sample valid image file
        self.valid_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00,'
                    b'\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;',
            content_type='image/jpeg'
        )
        self.valid_data = {'progress_image': self.valid_image}

        # Invalid data (no image file)
        self.invalid_data = {}

    # Test that the form initializes correctly
    def test_form_initialization(self):
        """Test that the form initializes correctly."""
        form = ProgressPictureForm()
        self.assertIn('progress_image', form.fields)

    # Test that the form is valid with correct data
    def test_form_valid_data(self):
        """Test that the form is valid with correct data."""
        form = ProgressPictureForm(data={}, files=self.valid_data)
        self.assertTrue(
            form.is_valid(),
            f"Expected form to be valid with data: {self.valid_data}"
        )

    # Test that the form validation fails for invalid file type
    def test_form_invalid_file_type(self):
        """Test that the form validation fails for invalid file type."""
        invalid_file = SimpleUploadedFile(
            name='test_file.txt',
            content=b'This is not an image.',
            content_type='text/plain'
        )
        invalid_data = {'progress_image': invalid_file}
        form = ProgressPictureForm(data={}, files=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('progress_image', form.errors)
        # Check if there's an error related to file type
        self.assertTrue(
            any("image" in error for error in form.errors['progress_image']),
            "Expected error about file type but got: {}".format(
                form.errors['progress_image']
            )
        )
