# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_auto_20150302_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyuser',
            name='phone',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
    ]
