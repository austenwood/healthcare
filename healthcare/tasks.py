import pandas as pd

from member_api.models import Member
from member_api.serializers import MemberSerializer

from .celery import app


@app.task()
def process_member_data(chunk):
    df = pd.read_json(chunk)
    row_iter = df.iterrows()

    member_data = [
        Member(
            first_name=row['first_name'],
            last_name=row['last_name'],
            phone_number=row['phone_number'],
            client_member_id=row['client_member_id'],
            account_id=row['account_id']
        ) for i, row in row_iter
    ]

    Member.objects.bulk_create(member_data)
