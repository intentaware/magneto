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

    def get(self, request, pk=None, email=None):
        if not pk:
            coupons = request.publisher.get_target_campaigns(request)
            impressions = list()
            visitor, created = ImpressionUser.objects.get_or_create(
                key=request.customer)
            meta = request.META
            meta.pop('wsgi.errors', None)
            meta.pop('wsgi.file_wrapper', None)
            meta.pop('wsgi.input', None)
            meta.pop('wsgi.version', None)
            meta = RequestEncoder().encode(meta)
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
            return Response(impressions, status=200)
        else:
            impression = Impression.objects.get(pk=pk)
            # get or create auth user based on email
            user, created = User.objects.get_or_create(email=email)
            # assign the user to impression object.
            impression.visitor.user = user
            impression.visitor.save()
            impression.save()
            impression.coupon.claim(user)
            return Response('claimed succesfully', status=200)


class ImpressionViewSet(ModelViewSet):
    serializer_class = ImpressionSerializer

    def get_queryset(self):
        return Impression.objects.all()
