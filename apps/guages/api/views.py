from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.authentication import BasicAuthentication
from apps.api.permissions import PublisherAPIPermission

class PostMatric(APIView):
    permission_classes = (PublisherAPIPermission,)
    authentication_classes = (BasicAuthentication,)


    def get(self, request, asset_id=None):
        raise MethodNotAllowed(self.request.method)

    def post(self, request, asset_id=None):
        #print asset_id
        from apps.guages.models import Asset, Matric
        from apps.users.models import Visitor
        asset = Asset.objects.get(key=asset_id)
        meta = request.data
        backends = self.process_request(request)
        backends.update(meta)
        #print request.visitor
        visitor, created = Visitor.objects.get_or_create(key=request.visitor)
        Matric.objects.create(
            asset = asset,
            meta = backends,
            visitor = visitor
        )
        return Response()

    def process_request(self, request):
        from ipware.ip import get_real_ip
        ip = get_real_ip(request) or '99.22.48.100'
        if ip:
            from geoip2 import database, webservice
            from django.conf import settings
            # client = webservice.Client(
            #     settings.MAXMIND_CLIENTID, settings.MAXMIND_SECRET)
            # ip2geo = client.insights(ip).raw
            # print ip2geo
            reader = database.Reader(settings.MAXMIND_CITY_DB)
            ip2geo = reader.city(ip).raw
        else:
            ip2geo = None
        user_agent = request.META['HTTP_USER_AGENT']
        return {
            'ip': ip,
            'user_agent': user_agent,
            'ip2geo': ip2geo,
        }

