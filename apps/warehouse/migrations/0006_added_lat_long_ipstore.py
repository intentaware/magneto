# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_postaldemographics'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipstore',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ipstore',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
