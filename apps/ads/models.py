from django.db import models
from django_extensions.db.fields import ShortUUIDField

from apps.common.models import TimeStamped, ToCompany


class Ad(TimeStamped, ToCompany):
    name = models.CharField(max_length=256, default='')
    description = models.TextField(null=True, blank=True)

    starts_on = models.DateTimeField(null=True, blank=True)
    ends_on = models.DateTimeField(null=True, blank=True)

    # for ad serving purposes
    counter = models.BigIntegerField(default=0)
    serve_limit = models.BigIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    is_coupon_ad = models.BooleanField(default=False)

    # an ad can be part of many industries, we will leverage django-taggit

    # call to action
    c2a = models.URLField(verbose_name='Call to Action')

    def increment(self):
        """
        increments the counter, whenever the ad is served
        """
        self.counter += self.counter
        self.save()


class Coupon(TimeStamped):
    code = ShortUUIDField()
    ad = models.ForeignKey('ads.Ad', related_name='coupons')
    redeemed_on = models.DateTimeField(null=True, blank=True)
    claimed_on = models.DateTimeField(null=True, blank=True)
    claimed_by = models.ForeignKey('users.User')

    def __unicode__(self):
        return 'Ad: %s, Coupon: %s' %(self.ad.name, self.code)

