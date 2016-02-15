from rest_framework.response import Response

from apps.companies.models import Company
from apps.api.viewsets import BaseModelViewSet

from .serializers import CompanySerializer, UpdateCompanySerializer


class CompanyViewSet(BaseModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.filter(
            id=self.request.session['company'])

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()

        s = UpdateCompanySerializer(instance, data=data, partial=True)
        if s.is_valid():
            self.perform_update(s)
            return Response(status=201)
        else:
            return Response(s.errors, 400)
