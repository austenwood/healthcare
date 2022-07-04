import pandas as pd
from rest_framework import generics, status
from rest_framework.response import Response

from healthcare.tasks import process_member_data

from .models import Member
from .serializers import FileUploadSerializer, MemberSerializer


class MemberListApiView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    # fields to allow filtering against
    filterset_fields = ['account_id', 'id', 'phone_number', 'client_member_id']

    def post(self, request):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'phone_number': request.data.get('phone_number'),
            'client_member_id': request.data.get('client_member_id'),
            'account_id': request.data.get('account_id')
        }

        serializer = MemberSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data['file']
        
        chunk_size = 5000

        with pd.read_csv(file, chunksize=chunk_size) as reader:
            for chunk in reader:
                serialized_chunk = chunk.to_json()
                process_member_data.delay(serialized_chunk)

        return Response({'status': 'success'}, status.HTTP_201_CREATED)
