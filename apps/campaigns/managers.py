from django.db.models import Manager, QuerySet


class CouponQuerySet(QuerySet):
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
                )
            c += 1
