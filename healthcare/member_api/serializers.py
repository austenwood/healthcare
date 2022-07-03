from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone_number',
                  'client_member_id', 'account_id']
        validators = [
            UniqueTogetherValidator(
                queryset=Member.objects.all(),
                fields=['phone_number', 'account_id']
            ),
            UniqueTogetherValidator(
                queryset=Member.objects.all(),
                fields=['phone_number', 'account_id']
            )
        ]


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
