from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import detail_route, list_route

from plugins.cities.models import City
from .serializers import CitySerializer

class CityViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CitySerializer

    class Meta:
        model = City

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            return City.objects.filter(name_std__icontains=name).prefetch_related('country')
        else:
            raise MethodNotAllowed('list', detail='Must contain query parameters')

    @list_route(methods=['get',])
    def search(self, request, *args, **kwargs):
        print args
        print kwargs
        return Response(status=200)
