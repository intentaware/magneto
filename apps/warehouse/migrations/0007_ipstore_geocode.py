# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_added_lat_long_ipstore'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipstore',
            name='geocode',
            field=django_pgjson.fields.JsonBField(null=True, blank=True),
        ),
    ]
