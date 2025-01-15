# Egyptian Phone Validator

A Django package to validate Egyptian phone numbers. 


## Features
- Validates Egyptian mobile phone numbers.

- Ensures the phone number is exactly 11 digits long.

- Checks for valid Egyptian mobile prefixes.

- Raises ValidationError for invalid phone numbers.

- Ensures the phone number is digits.


## Installation

Install the package using pip:

```bash
pip install egyptian-phone-validator
```


## Usage

```bash
from django.db import models
from egyptian_phone_validator.validators import validate_egyptian_phone_number

class UserProfile(models.Model):
    phone = models.CharField(
        max_length=11,
        validators=[validate_egyptian_phone_number],
        help_text="Enter a valid Egyptian phone number (e.g., 01012345678)."
    )
```


## PyPI Package

You can find the `egyptian-phone-validator` package on PyPI. Click the link below to visit the project page:

[![PyPI Version](https://img.shields.io/pypi/v/egyptian-phone-validator?color=blue&label=PyPI%20Package)](https://pypi.org/project/egyptian-phone-validator/)
