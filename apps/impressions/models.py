from django.db import models
from django_pgjson.fields import JsonField
from django_extensions.db.fields import *

from apps.common.models import TimeStamped


class ImpressionUser(TimeStamped):
    user = models.ForeignKey('users.User', blank=True, null=True)
    key = ShortUUIDField()
    has_opted_out = models.BooleanField(default=False)

    def set_opt_out_flag(self):
        self.has_opted_out = True
        self.save()

    def __unicode__(self):
        return self.key


class Impression(TimeStamped):
    campaign = models.ForeignKey('campaigns.Campaign', related_name='impressions')
    coupon = models.ForeignKey('campaigns.Coupon', related_name='impressions')
    meta = JsonField(blank=True, null=True)
    visitor = models.ForeignKey(ImpressionUser, related_name='impressions')
    publisher = models.ForeignKey('companies.Company', related_name='impressions')

    def create_from_request(self, request, campaign):
        self.campaign = campaign
        self.meta = request._request.META
        self.visitor, created = ImpressionUser.objects.get_or_create(key=request.customer)
        self.publisher = request.publisher

    def __unicode__(self):
        return '%s: %s' %(self.campaign, self.id)

    def hydrate_meta(self):
        meta = self.meta
        self.meta['impression'] = self.id
        ip2geo = meta.pop('ip2geo')
        self.meta['city'] = ip2geo['city']['names']['en']
        self.meta['country'] = ip2geo['country']['names']['en']
        self.meta['postal_code'] = ip2geo['postal']['code']
        self.meta['latitude'] = ip2geo['location']['latitude']
        self.meta['longitude'] = ip2geo['location']['longitude']

