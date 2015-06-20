# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0010_auto_20150415_1313'),
        ('impressions', '0007_auto_20150331_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='coupon',
            field=models.ForeignKey(related_name='impressions', default=1, to='campaigns.Coupon'),
            preserve_default=False,
        ),
    ]
