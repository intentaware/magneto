# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0011_impressionuser_has_opted_out'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='impression',
        #     name='meta',
        #     field=django_pgjson.fields.JsonBField(null=True, blank=True),
        # ),
        migrations.RunSQL(
                'ALTER TABLE impressions_impression ALTER COLUMN meta SET DATA TYPE jsonb USING meta::jsonb;'
            ),
    ]
