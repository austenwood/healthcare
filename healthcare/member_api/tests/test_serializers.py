import pytest

from member_api.serializers import MemberSerializer


@pytest.mark.django_db
def test_valid_member_serializer():
    valid_serializer_data = {
        'first_name': 'Yank',
        'last_name': 'Deboo',
        'phone_number': '1284628753',
        'client_member_id': 9436555,
        'account_id': 12
    }
    serializer = MemberSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_member_serializer():
    invalid_serializer_data = {
        'first_name': 'Yank',
        'last_name': 'Deboo',
        'client_member_id': 9436555,
        'account_id': 12
    }
    serializer = MemberSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {'phone_number': ['This field is required.']}
