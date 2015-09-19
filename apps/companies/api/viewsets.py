from apps.companies.models import Company
from apps.api.viewsets import BaseModelViewSet

from .serializers import CompanySerializer


class CompanyViewSet(BaseModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.filter(
            id=self.request.session['company'])
