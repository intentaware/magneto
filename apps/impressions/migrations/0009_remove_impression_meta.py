# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0008_impression_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impression',
            name='meta',
        ),
    ]
