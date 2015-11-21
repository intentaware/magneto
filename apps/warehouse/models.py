from django.db import models

from apps.common.models import TimeStamped
from plugins.cities.models import PostalCode


class IPStore(TimeStamped):
    ip = models.GenericIPAddressField(unpack_ipv4=True)
    postal_code = models.ForeignKey('cities.PostalCode', blank=True, null=True)

    def __unicode__(self):
        return self.ip

    @property
    def verbose_postal_code(self):
        return '%s - %s' %(self.postal_code.code, self.postal_code.country.name)


class PostalDemographics(TimeStamped):
    postal_code = models.ForeignKey('cities.PostalCode')
    income_per_capita = models.PositiveIntegerField(blank=True, null=True)
    income_household = models.PositiveIntegerField(blank=True, null=True)
