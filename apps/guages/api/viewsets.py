from apps.api.viewsets import BaseModelViewSet
from .serializers import AssetSerializer
from apps.guages.models import Asset

class AssetViewSet(BaseModelViewSet):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.filter(
            publisher_id=self.request.session['company'])
