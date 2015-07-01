from rest_framework import viewsets
from rest_framework.response import Response

from apps.campaigns.models import Campaign
from .serializers import CampaignSerializer, CreateCampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    #queryset = Campaign.objects.prefetch_related('image').all()

    def get_queryset(self):
        return Campaign.objects.prefetch_related(
                'image', 'coupons', 'invoice', 'coupons__impressions',
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


    def partial_update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        s = CreateCampaignSerializer(instance, data=data, partial=True)
        s.is_valid(raise_exception=True)
        self.perform_update(s)
        return Response(s.data)
