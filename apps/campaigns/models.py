from django.db import models
from django_extensions.db.fields import ShortUUIDField

from apps.common.models import TimeStamped, ToCompany
from .managers import CouponManager


class Campaign(TimeStamped, ToCompany):
    """
    inherits created_on, updated_on and company fields
    """
    name = models.CharField(max_length=256, default='')
    description = models.TextField(null=True, blank=True)

    # starts_on = models.DateTimeField(null=True, blank=True)
    # ends_on = models.DateTimeField(null=True, blank=True)

    # set if it is a coupon ad
    is_coupon_ad = models.BooleanField(default=False)

    # for ad serving purposes
    # counter = models.BigIntegerField(default=0)
    # serve_limit = models.BigIntegerField(default=100)

    budget = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)
    coupon_value = models.DecimalField(default=0.0, max_digits=20, decimal_places=4)

    # set the ad to inactive after the limit is served
    is_active = models.BooleanField(default=True)

    # an ad can be part of many industries, we will leverage django-taggit

    # call to action
    c2a = models.URLField(verbose_name='Call to Action')

    # photologue
    image = models.ForeignKey('photologue.Photo', related_name='campaigns', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        saved = False
        if self.id:
            saved = True
        campaign = super(Campaign, self).save(*args, **kwargs)
        return campaign


class Coupon(TimeStamped, ToCompany):
    code = ShortUUIDField()
    campaign = models.ForeignKey(Campaign, related_name='coupons')
    redeemed_on = models.DateTimeField(null=True, blank=True)
    claimed_on = models.DateTimeField(null=True, blank=True)
    """
    What is the difference between claimed on and redeemed_on?
    redeemed_on = when the coupon is assigned a user,
    claimed_on = when the coupon is verified and discount is approved
    """
    claimed_by = models.ForeignKey('users.User', blank=True, null=True)

    # custom manager
    objects = CouponManager()

    def __unicode__(self):
        return 'Campaign: %s, Coupon: %s' %(self.campaign.name, self.code)
