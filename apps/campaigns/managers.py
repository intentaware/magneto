from django.db.models import Manager, QuerySet

class CouponManager(Manager):
    use_for_related_fields = True

    def generate(self, campaign, count):
        print campaign
        c = 0
        while c < count:
            self.create(
                    campaign = campaign,
                    company = campaign.company,
                )
            c += 1
