from rest_framework import serializers
from .models import Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone_number', 'client_member_id', 'account_id']