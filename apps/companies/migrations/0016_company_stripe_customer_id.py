# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_auto_20150515_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='stripe_customer_id',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
