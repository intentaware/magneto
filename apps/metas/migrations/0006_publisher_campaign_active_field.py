# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0005_populate_circle_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigncircle',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='publishercircle',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
