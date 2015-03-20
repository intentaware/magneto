from rest_framework import viewsets
from rest_framework.response import Response

from apps.campaigns.models import Campaign
from .serializers import CampaignSerializer, CreateCampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

    def create(self, request):
        # print request.data
        s = CreateCampaignSerializer(data=request.data)
        if s.is_valid():
            c = s.save()
            return Response(CampaignSerializer(c).data)
        else:
            return Response(s.errors, status=400)
