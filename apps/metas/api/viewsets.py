from rest_framework import viewsets
from apps.metas.models import Circle, CampaignCircle, PublisherCircle
from .serializers import CircleSerializer, CampaignCircleSerializer


class CircleViewSet(viewsets.ModelViewSet):
    serializer_class = CircleSerializer

    def get_queryset(self):
        return Circle.objects.all()


class CampaignCircleViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignCircleSerializer

    def get_queryset(self):
        return CampaignCircle.objects.all()
