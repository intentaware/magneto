from rest_framework import viewsets

from apps.companies.models import Company, Circle
from .serializers import CompanySerializer, CircleSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.filter(
            id=self.request.session['company'])


class CircleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CircleSerializer
    queryset = Circle.objects.all()
