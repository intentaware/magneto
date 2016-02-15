# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0009_remove_impression_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='meta',
            field=django_pgjson.fields.JsonField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
