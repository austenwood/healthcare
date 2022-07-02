from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    client_member_id = models.IntegerField()
    account_id = models.IntegerField()

class Provider(models.Model):
    account_id = models.IntegerField()
    members = models.ManyToManyField(Member)