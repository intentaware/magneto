from django.db import models
from jsonfield.fields import JSONField
from django_extensions.db.fields import *

from apps.common.models import TimeStamped


class ImpressionUser(TimeStamped):
    user = models.ForeignKey('users.User', blank=True, null=True)
    key = ShortUUIDField()

    def __unicode__(self):
        return self.key


class Impression(TimeStamped):
    campaign = models.ForeignKey('campaigns.Campaign', related_name='impressions')
    meta = JSONField(blank=True, null=True)
    visitor = models.ForeignKey(ImpressionUser, related_name='impressions')
    publisher = models.ForeignKey('companies.Company', related_name='impressions')

    def create_from_request(self, request, campaign):
        self.campaign = campaign
        self.meta = request._request.META
        self.visitor, created = ImpressionUser.objects.get_or_create(key=request.customer)
        self.publisher = request.publisher

    def __unicode__(self):
        return '%s: %s' %(self.campaign, self.id)
