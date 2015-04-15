# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0009_campaign_coupon_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='c2a',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='is_coupon_ad',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='coupon_value',
            field=models.DecimalField(default=1, max_digits=20, decimal_places=4),
            preserve_default=True,
        ),
    ]
