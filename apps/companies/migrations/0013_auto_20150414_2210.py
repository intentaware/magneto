# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_auto_20150414_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='impressions_per_dollar',
        ),
        migrations.AddField(
            model_name='company',
            name='advertiser_rate',
            field=models.FloatField(default=0.25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='publisher_rate',
            field=models.FloatField(default=0.05),
            preserve_default=True,
        ),
    ]
