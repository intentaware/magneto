from rest_framework import viewsets

from apps.campaigns.models import Campaign
from .serializers import CreateCampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CreateCampaignSerializer
    queryset = Campaign.objects.all()
