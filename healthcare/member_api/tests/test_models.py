import pytest

from member_api.models import Member


@pytest.mark.django_db
def test_member_model():
    member = Member(first_name='Yank', last_name='Deboo',
                    phone_number='1284628753', client_member_id=9436555,
                    account_id=12)
    member.save()
    assert member.first_name == 'Yank'
    assert member.last_name == 'Deboo'
    assert member.phone_number == '1284628753'
    assert member.client_member_id == 9436555
    assert member.account_id == 12
