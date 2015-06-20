# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0016_campaign_coupon_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
