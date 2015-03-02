from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, CompanyRegistrationSerializer


class UserRegistrationView(APIView):

    def post(self, request):
        user = UserRegistrationSerializer(data=request.data)
        if user.is_valid():
            user = user.save()
            return Response({
                'user': user.id
            }, status=201)
        else:
            return Response(user.errors, status=400)


class CompanyRegistrationView(APIView):

    def post(self, request):
        company = CompanyRegistrationSerializer(data=request.data)
        if company.is_valid():
            company = company.save()
            return Response({
                'company': company.id
            }, status=201)
        else:
            return Response(company.errors, status=400)