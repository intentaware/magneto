from rest_framework.views import APIView
from rest_framework.response import Response

from apps.api.permissions import UserRegistrationAPIPermission, \
    PublisherAPIPermission
from .serializers import UserRegistrationSerializer, \
    CompanyRegistrationSerializer

class UserRegistrationView(APIView):
    permission_classes = (PublisherAPIPermission, )

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": user.id
            }, status=201)
        else:
            return Response(serializer.errors, status=400)


class CompanyRegistrationView(APIView):
    permission_classes = (UserRegistrationAPIPermission, )

    def post(self, request):
        serializer = CompanyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.save()
            return Response({
                'company': member.company.id
            }, status=201)
        else:
            return Response(serializer.errors, status=400)
