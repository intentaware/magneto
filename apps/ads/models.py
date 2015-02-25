from django.db import models
from apps.common.models import *


class Ad(SulggedFromTitle, TimeStamped):
    description = models.TextField(null=True, blank=True)

    starts_on = models.DateTimeField(null=True, blank=True)
    ends_on = models.DateTimeField(null=True, blank=True)

    #for ad serving purposes
    counter = models.BigIntegerField(default=0)
    serve_limit = models.BigIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    #an ad can be part of many industries, we will leverage django-taggit

    def increment(self):
        '''
        increments the counter, whenever the ad is served
        '''
        self.counter += self.counter
        self.save()