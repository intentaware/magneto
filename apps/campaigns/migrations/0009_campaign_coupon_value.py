# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0008_auto_20150414_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='coupon_value',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=4),
            preserve_default=True,
        ),
    ]
