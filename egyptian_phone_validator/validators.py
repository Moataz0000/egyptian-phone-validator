import re
from django.core.exceptions import ValidationError




def validate_egyptian_phone_number(value):
    """
    Validates that the phone number is a valid Egyptian mobile number.
    """
    
    if not value:
        raise ValidationError('Phone number can not be empty!')
    
    value.strip()
    
    if not value.isdigit():
        raise ValidationError('Phone number must contain only digits!')
    
    if len(value) != 11:
        raise ValidationError('Phone number must be exactly 11 digits long!')
    
    egyptian_codes = ['010', '011', '012', '015']
    if value[:3] not in egyptian_codes:
        raise ValidationError(f'Phone number must begin with one of these codes: {egyptian_codes}!')
    