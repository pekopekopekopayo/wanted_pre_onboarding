import re
from django.db import models
from django.core.validators import RegexValidator
from django.forms import ValidationError

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone_number_regex = RegexValidator(regex = r'^01([0|1|6|7|8|9])([0-9]{4})([0-9]{4})', message='Not a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=11, unique=True, null=False, blank=False)


    def full_clean(self):
        self.phone_number = re.sub('[-]', '', str(self.phone_number))

        super().full_clean()
        
