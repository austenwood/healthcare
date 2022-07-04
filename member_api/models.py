from django.db import models
from django.core.validators import RegexValidator


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'\d{8,15}$',
                                 message='Phone number must be entered in the format: 9999999999. Up to 15 digits allowed.')
    phone_number = models.CharField(validators=[phone_regex], max_length=16)
    client_member_id = models.IntegerField()
    account_id = models.IntegerField()
