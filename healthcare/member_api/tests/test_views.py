import json

import pytest

from member_api.models import Member


@pytest.mark.django_db
def test_add_member(client):
    members = Member.objects.all()
    assert len(members) == 0

    response = client.post(
        '/api/members/',
        {
            'first_name': 'Yank',
            'last_name': 'Deboo',
            'phone_number': '1284628753',
            'client_member_id': 9436555,
            'account_id': 12
        },
        content_type='application/json'
    )
    assert response.status_code == 201
    assert response.data['phone_number'] == '1284628753'

    members = Member.objects.all()
    assert len(members) == 1


@pytest.mark.django_db
def test_add_member_invalid_json(client):
    members = Member.objects.all()
    assert len(members) == 0

    response = client.post(
        '/api/members/',
        {},
        content_type='application/json'
    )
    assert response.status_code == 400

    members = Member.objects.all()
    assert len(members) == 0


@pytest.mark.django_db
def test_add_member_invalid_json_keys(client):
    members = Member.objects.all()
    assert len(members) == 0

    response = client.post(
        '/api/members/',
        {
            'first_name': 'Yank',
            'last_name': 'Deboo',
            'client_member_id': 9436555,
            'account_id': 12
        },
        content_type='application/json'
    )
    assert response.status_code == 400

    members = Member.objects.all()
    assert len(members) == 0


@pytest.mark.django_db
def test_get_single_member(client):
    member = Member.objects.create(first_name='Yank', last_name='Deboo',
                                   phone_number='1284628753', 
                                   client_member_id=9436555, account_id=12)
    response = client.get(f'/api/members/?id={member.id}.')
    assert response.status_code == 200
    assert response.data[0]['phone_number'] == '1284628753'
