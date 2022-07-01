from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    client_member_id = models.IntegerField()
    account_id = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Provider(models.Model):
    account_id = models.IntegerField()
    members = models.ManyToManyField(Member)