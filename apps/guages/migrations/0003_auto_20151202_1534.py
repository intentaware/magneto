# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('guages', '0002_matric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matric',
            name='meta',
            field=django_pgjson.fields.JsonBField(null=True, blank=True),
        ),
    ]
