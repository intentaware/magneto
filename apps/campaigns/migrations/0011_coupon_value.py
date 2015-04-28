# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0010_auto_20150415_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='value',
            field=models.DecimalField(default=1, max_digits=20, decimal_places=4),
            preserve_default=True,
        ),
    ]
