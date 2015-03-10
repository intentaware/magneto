from django.db import models
from django_extensions.db.fields import ShortUUIDField

from apps.common.models import TimeStamped, ToCompany


class Campaign(TimeStamped, ToCompany):
    name = models.CharField(max_length=256, default='')
    description = models.TextField(null=True, blank=True)

    starts_on = models.DateTimeField(null=True, blank=True)
    ends_on = models.DateTimeField(null=True, blank=True)

    # set if it is a coupon ad
    is_coupon_ad = models.BooleanField(default=False)

    # for ad serving purposes
    counter = models.BigIntegerField(default=0)
    serve_limit = models.BigIntegerField(default=100)

    # set the ad to inactive after the limit is served
    is_active = models.BooleanField(default=True)

    # an ad can be part of many industries, we will leverage django-taggit

    # call to action
    c2a = models.URLField(verbose_name='Call to Action')


    def increment(self):
        """
        increments the counter, whenever the ad is served
        """
        self.counter += self.counter
        self.save()

    @property
    def coupon_serve_limit(self):
        """
        Implement a method to get a cut of on serve limit
        it will be mix of number of impressions, and number of coupon
        served
        :return:
        """


class Coupon(TimeStamped):
    code = ShortUUIDField()
    campaign = models.ForeignKey(Campaign, related_name='coupons')
    redeemed_on = models.DateTimeField(null=True, blank=True)
    claimed_on = models.DateTimeField(null=True, blank=True)
    claimed_by = models.ForeignKey('users.User')

    def __unicode__(self):
        return 'Ad: %s, Coupon: %s' %(self.ad.name, self.code)
