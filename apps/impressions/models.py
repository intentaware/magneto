from django.db import models
from jsonfield.fields import JSONField

from apps.common.models import TimeStamped


class Impression(TimeStamped):
    ad = models.ForeignKey('ads.Ad', related_name='impressions')
    data = JSONField(blank=True, null=True)

    # if the impression is made from an already logged in user
    user = models.ForeignKey('users.User', related_name='impressions')