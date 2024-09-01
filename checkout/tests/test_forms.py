# Import necessary modules and classes for testing
from django.test import TestCase
from checkout.forms import OrderForm


# Define test cases for the OrderForm
class OrderFormTest(TestCase):

    def setUp(self):
        # Sample valid data for testing the form
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890'
        }

    # Test that the form initializes correctly with the expected attributes
    def test_form_initialization(self):
        """
        Test that the form initializes
        correctly with the expected attributes.
        """
        form = OrderForm()  # Initialize the form without data
        # Check that each field in the form has the correct attributes
        for field_name, field in form.fields.items():
            self.assertIn('class', field.widget.attrs)
            self.assertEqual(field.widget.attrs['class'], 'form-control')
            self.assertIn('required', field.widget.attrs)
            self.assertTrue(field.widget.attrs['required'])

    # Test that the form is valid with correct data
    def test_form_valid_data(self):
        """Test that the form is valid with correct data."""
        form = OrderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())  # Check that the form is valid

    # Test first name validation with valid input
    def test_clean_first_name_valid(self):
        """Test first name validation with valid input."""
        form = OrderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())  # Check that the form is valid
        self.assertEqual(form.cleaned_data['first_name'], 'John')

    # Test first name validation with invalid input (non-alphabetic characters)
    def test_clean_first_name_invalid(self):
        """Test first name validation with invalid input."""
        data = self.valid_data.copy()
        data['first_name'] = 'John123'
        form = OrderForm(data=data)  # Initialize the form with invalid data
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        self.assertIn('first_name', form.errors)
        self.assertEqual(
            form.errors['first_name'],
            ['First name should only contain alphabetic characters.']
        )

    # Test last name validation with valid input
    def test_clean_last_name_valid(self):
        """Test last name validation with valid input."""
        form = OrderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())  # Check that the form is valid
        self.assertEqual(form.cleaned_data['last_name'], 'Doe')

    # Test last name validation with invalid input (non-alphabetic characters)
    def test_clean_last_name_invalid(self):
        """Test last name validation with invalid input."""
        data = self.valid_data.copy()
        data['last_name'] = 'Doe123'
        form = OrderForm(data=data)  # Initialize the form with invalid data
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        self.assertIn('last_name', form.errors)
        self.assertEqual(
            form.errors['last_name'],
            ['Last name should only contain alphabetic characters.']
        )

    # Test phone number validation with valid input
    def test_clean_phone_number_valid(self):
        """Test phone number validation with valid input."""
        form = OrderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())  # Check that the form is valid
        self.assertEqual(form.cleaned_data['phone_number'], '1234567890')

    # Test phone number validation with invalid input (non-numeric characters)
    def test_clean_phone_number_invalid(self):
        """Test phone number validation with invalid input."""
        data = self.valid_data.copy()
        data['phone_number'] = '123-456-7890'
        form = OrderForm(data=data)  # Initialize the form with invalid data
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        self.assertIn('phone_number', form.errors)
        self.assertEqual(
            form.errors['phone_number'],
            ['Phone number should only contain numeric characters.']
        )

    # Test phone number validation with an empty input
    def test_clean_phone_number_empty(self):
        """Test phone number validation with an empty input."""
        data = self.valid_data.copy()
        data['phone_number'] = ''  # Empty phone number input
        form = OrderForm(data=data)  # Initialize the form with invalid data
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        self.assertIn('phone_number', form.errors)
        self.assertEqual(
            form.errors['phone_number'],
            ['Phone number should only contain numeric characters.']
        )
