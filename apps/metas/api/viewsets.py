from apps.api.viewsets import BaseModelViewSet
from apps.metas.models import Circle, CampaignCircle, PublisherCircle
from .serializers import CircleSerializer, CampaignCircleSerializer


class CircleViewSet(BaseModelViewSet):
    serializer_class = CircleSerializer

    def get_queryset(self):
        return Circle.objects.all()


class CampaignCircleViewSet(BaseModelViewSet):
    serializer_class = CampaignCircleSerializer

    def get_queryset(self):
        return CampaignCircle.objects.all()
