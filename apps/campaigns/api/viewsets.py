from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from apps.campaigns.models import Campaign
from apps.api.viewsets import BaseModelViewSet
from .serializers import CampaignSerializer, CreateCampaignSerializer


class CampaignViewSet(BaseModelViewSet):
    serializer_class = CampaignSerializer
    #queryset = Campaign.objects.prefetch_related('image').all()

    def get_queryset(self):
        return Campaign.objects.prefetch_related(
                'image', 'coupons', 'invoice', 'coupons__impressions',
            ).filter(
                company_id=self.request.session['company']
            ).active()

    def create(self, request):
        data = request.data
        data['company'] = request.session['company']
        s = CreateCampaignSerializer(data=request.data)
        if s.is_valid():
            c = s.save()
            return Response(CampaignSerializer(c).data)
        else:
            return Response(s.errors, status=400)


    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        # print instance
        s = CreateCampaignSerializer(instance, data=data, partial=True)
        # print s
        if s.is_valid():
            self.perform_update(s)
            return Response(status=201)
        else:
            return Response(s.errors, 400)

    @list_route(methods=['get',])
    def past(self, request, *args, **kwargs):
        return Response(
                CampaignSerializer(Campaign.objects.inactive(), many=True).data, 200
            )
