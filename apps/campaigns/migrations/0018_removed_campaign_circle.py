# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0017_campaign_is_active_default_is_false'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaigncircle',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='campaigncircle',
            name='circle',
        ),
        migrations.DeleteModel(
            name='CampaignCircle',
        ),
    ]
