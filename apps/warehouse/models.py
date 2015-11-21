from django.db import models

from apps.common.models import TimeStamped
from plugins.cities.models import PostalCode


class IPStore(TimeStamped):
    ip = models.GenericIPAddressField(unpack_ipv4=True)
    postal_code = models.OneToOneField('cities.PostalCode', blank=True, null=True)

    def __unicode__(self):
        return self.ip
