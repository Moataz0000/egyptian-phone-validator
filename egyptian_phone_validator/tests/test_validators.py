from django.core.exceptions import ValidationError
from django.test import TestCase
from egyptian_phone_validator.validators import validate_egyptian_phone_number





class EgyptianPhoneValidatorTests(TestCase):
    def test_valid_phone_number(self):
        valid_numbers = ['01012345678', '01198765432', '01234567890', '01555555555']
        for number in valid_numbers:
            with self.subTest(number=number):
                validate_egyptian_phone_number(number)
                
    def test_invalid_phone_numbers(self):
        invalid_numbers = ['', '0101234567', '011987654321', '0123456789a', '01912345678']
        for number in invalid_numbers:
            with self.subTest(number=number):
                with self.assertRaises(ValidationError):
                    validate_egyptian_phone_number(number)