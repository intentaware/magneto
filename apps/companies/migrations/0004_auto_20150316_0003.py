# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150310_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_advertiser',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='is_publisher',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
