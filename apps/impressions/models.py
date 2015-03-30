from django.db import models
from jsonfield.fields import JSONField
from django_extensions.db.fields import *

from apps.common.models import TimeStamped


class ImpressionUser(TimeStamped):
    user = models.ForeignKey('users.User', blank=True, null=True)
    key = ShortUUIDField()


class Impression(TimeStamped):
    campaign = models.ForeignKey('campaigns.Campaign', related_name='impressions')
    meta = JSONField(blank=True, null=True)
    user = models.ForeignKey(ImpressionUser, related_name='impressions')
    pubisher = models.ForeignKey('companies.Company', related_name='impressions')

    def new(self, request):
        p = request.pubisher
        return pubisher
