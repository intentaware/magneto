# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0003_model_publisher_cirlce'),
        ('campaigns', '0018_removed_campaign_circle'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='circles',
            field=models.ManyToManyField(to='metas.Circle', through='metas.CampaignCircle'),
        ),
    ]
