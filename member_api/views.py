from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .models import Member
from .serializers import MemberSerializer


class MemberListApiView(generics.ListAPIView):
    # check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    filterset_fields = ['account_id', 'id', 'phone_number', 'client_member_id']

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'phone_number': request.data.get('phone_number'),
            'client_member_id': request.data.get('client_member_id'),
            'account_id': request.data.get('account_id')
        }

        serializer = MemberSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)