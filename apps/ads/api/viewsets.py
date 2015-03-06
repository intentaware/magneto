from rest_framework import viewsets

from apps.ads.models import Ad
from .serializers import CreateAdSerializer


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = CreateAdSerializer
    queryset = Ad.objects.all()
