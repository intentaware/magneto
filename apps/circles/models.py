from django.db import models
from apps.common.models import *

class Circle(TimeStamped):
    parent = models.ForeignKey('self', related_name="children")
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name
