from json import JSONEncoder

from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.api.permissions import PublisherAPIPermission
from apps.impressions.models import Impression, ImpressionUser
from apps.users.models import User

from .serializers import ImpressionSerializer


class RequestEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class GetImpression(APIView):
    permission_classes = (PublisherAPIPermission,)

    def get(self, request, pk=None, b64_string=None):
        if not pk:
            coupons = request.publisher.get_target_campaigns(request)
            # TODO: when we are done with legace, pinpoint a single coupon
            impressions = self.get_impression_markup(request, coupons)
            return Response(impressions, status=200)
        else:
            try:
                impression = Impression.objects.get(pk=pk)
                # get or create auth user based on email
                if b64_string:
                    key, val = self.process_base64(b64_string, impression)
                    if key == 'email':
                        self.claim_coupon(impression, val)
                    return Response('claimed successfully', status=200)
            except Impression.DoesNotExist:
                if b64_string:
                    key, val = self.process_base64(b64_string)
                    if key == "campaign":
                        coupons = request.publisher.get_target_campaigns(request, campaign_id=val)
                        impressions = self.get_impression_markup(request, coupons)
                        return Response(impressions, status=200)

    def get_impression_markup(self, request, coupons):
        impressions = list()
        visitor, created = ImpressionUser.objects.get_or_create(
            key=request.customer)
        if request.user.is_authenticated() and not visitor.user:
            visitor.user = request.user
            visitor.save()
        meta = self.process_request(request)
        # print meta
        for c in coupons:
            i = Impression.objects.create(
                coupon=c, campaign=c.campaign, publisher=request.publisher,
                visitor=visitor, meta=meta
            )
            template = render_to_string('impressions/basic.html', {
                'impression': i
            })
            impression = {
                'id': i.id,
                'template': template
            }
            impressions.append(impression)
        return impressions

    def process_base64(self, b64_string, impression):
        import base64, json
        data = json.loads(base64.b64decode(b64_string))
        email = data.get('email', None)
        meta = data.get('meta', None)
        if email:
            #print email
            return 'email', email
        elif meta:
            meta = json.loads(meta)
            self.update_meta(meta, impression)
            return 'key', 'val'

    def update_meta(self, dictionary, impression):
        """updated the impression meta data

        Args:
            dictionary (dict): dictionary of items
            impression (object): impression model object on which the data needs
            to be updated

        Returns:
            None: returns nothing
        """
        for key, val in dictionary.iteritems():
            impression.meta[key] = val
        impression.save()


    def claim_coupon(self, impression, email):
        user, created = User.objects.get_or_create(email=email)
        # assign the user to impression object.
        impression.visitor.user = user
        impression.visitor.save()
        impression.save()
        impression.coupon.claim(user)

    def process_request(self, request):
        from ipware.ip import get_real_ip
        ip = get_real_ip(request) or '99.22.48.100'
        if ip:
            import geoip2.webservice
            from django.conf import settings
            client = geoip2.webservice.Client(
                settings.MAXMIND_CLIENTID, settings.MAXMIND_SECRET)
            #reader = geoip2.database.Reader(settings.MAXMIND_CITY_DB)
            ip2geo = client.insights(ip).raw
            print ip2geo
            #ip2geo = reader.city(ip).raw
        else:
            ip2geo = None
        user_agent = request.META['HTTP_USER_AGENT']
        return {
            'ip': ip,
            'user_agent': user_agent,
            'ip2geo': ip2geo,
        }
