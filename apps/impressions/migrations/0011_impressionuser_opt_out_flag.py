# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0010_impression_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='impressionuser',
            name='opt_out_flag',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
