# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0013_auto_20150414_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='advertiser_rate',
            field=models.DecimalField(default=0.25, max_digits=20, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='publisher_rate',
            field=models.DecimalField(default=0.05, max_digits=20, decimal_places=4),
            preserve_default=True,
        ),
    ]
