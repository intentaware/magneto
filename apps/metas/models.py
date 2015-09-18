from django.db import models
from apps.common.models import *

class Circle(TimeStamped):
    parent = models.ForeignKey('self', blank=True, null=True, related_name="children")
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class PublisherCircle(TimeStamped):
    publisher = models.ForeignKey('companies.Company')
    circle = models.ForeignKey('metas.Circle')

    class Meta:
        unique_together=['publisher', 'circle']


class CampaignCircle(TimeStamped):
    campaign = models.ForeignKey('campaigns.Campaign')
    circle = models.ForeignKey('metas.Circle')

    class Meta:
        unique_together = ['campaign', 'circle']
