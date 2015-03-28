from rest_framework.views import APIView
from rest_framework.response import Response

from apps.api.permissions import PublisherAPIPermission


class GetImpression(APIView):
    permission_classes = (PublisherAPIPermission,)

    def get(self, request):
        return Response({
                'impression': '1'
            }, status=201)

