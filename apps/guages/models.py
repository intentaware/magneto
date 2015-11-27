from django.db import models
from django_pgjson.fields import JsonBField
from django_extensions.db.fields import ShortUUIDField


from apps.common.models import TimeStamped
# Create your models here.

class Asset(TimeStamped):
    name = models.CharField(max_length=128)
    url = models.URLField()
    key = ShortUUIDField()
    publisher = models.ForeignKey('companies.Company', related_name='assets')


class Matric(TimeStamped):
    asset = models.ForeignKey('guages.Asset', related_name='matrices')
    visitor = models.ForeignKey('users.Visitor', related_name='matrics')
    meta = JsonBField()
