# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postalcode',
            name='income_household',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='postalcode',
            name='income_per_capita',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
