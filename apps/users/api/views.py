from rest_framework.views import APIView
from rest_framework.response import Response
from registration import signals

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
            signals.user_registered.send(
                sender=self.__class__,
                user=user,
                request=request
            )
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
            signals.user_registered.send(
                sender=self.__class__,
                user=member.user,
                request=request
            )
            return Response({
                'company': member.company.id
            }, status=201)
        else:
            return Response(serializer.errors, status=400)
