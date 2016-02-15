from __future__ import absolute_import
from adomattic.celery import app as capp


@capp.task
def generate_coupons(campaign_id, count):
    from apps.campaigns.models import Campaign, Coupon
    campaign = Campaign.objects.get(id=campaign_id)
    Coupon.objects.generate(campaign, count)
    return
