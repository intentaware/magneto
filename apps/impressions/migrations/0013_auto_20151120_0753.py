# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0012_update_meta_to_jsonb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impression',
            name='meta',
            field=django_pgjson.fields.JsonBField(null=True, blank=True),
        ),
    ]
