from django.db.models import Manager, QuerySet, Sum


class CampaignQuerySet(QuerySet):
    """
    custom manager for 'Campaign' model
    """
    def active(self):
        return self.filter(is_active=True)

    def active_budget(self):
        return self.aggregate(Sum('budget'))['budget__sum']


class CampaignManager(Manager):
    use_for_related_fields = True


class CouponQuerySet(QuerySet):
    def active(self):
        return self.filter(campaign__is_active=True)

    def claimed(self):
        return self.filter(claimed_on__isnull=False)

    def remaining(self):
        return self.filter(claimed_on__isnull=True)


class CouponManager(Manager):
    use_for_related_fields = True

    def generate(self, campaign, count):
        c = 0
        while c < count:
            self.create(
                    campaign = campaign,
                    company = campaign.company,
                    value = campaign.coupon_value
                )
            c += 1
