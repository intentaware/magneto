# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0015_campaign_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='coupon_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
