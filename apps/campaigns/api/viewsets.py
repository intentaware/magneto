from rest_framework import viewsets
from rest_framework.response import Response

from apps.campaigns.models import Campaign
from .serializers import CampaignSerializer, CreateCampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    #queryset = Campaign.objects.prefetch_related('image').all()

    def get_queryset(self):
        return Campaign.objects.prefetch_related(
                'image', 'coupons', 'invoice',
            ).filter(
                company_id=self.request.session['company']
            )

    def create(self, request):
        data = request.data
        data['company'] = request.session['company']
        s = CreateCampaignSerializer(data=request.data)
        if s.is_valid():
            c = s.save()
            return Response(CampaignSerializer(c).data)
        else:
            return Response(s.errors, status=400)
