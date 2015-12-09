from rest_framework.response import Response

from apps.api.viewsets import BaseModelViewSet
from .serializers import AssetSerializer, CreateAssetSerializer
from apps.guages.models import Asset

class AssetViewSet(BaseModelViewSet):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.prefetch_related(
                    'metrics'
                ).filter(
                    publisher_id=self.request.session['company']
                )

    def create(self, request):
        data = request.data
        data['publisher'] = request.session['company']
        s = CreateAssetSerializer(data=data)
        if s.is_valid():
            asset = s.save()
            return Response(AssetSerializer(asset).data, status=201)
        else:
            return Response(s.errors, status=400)
