# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20150316_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='publisher_key',
            field=django_extensions.db.fields.ShortUUIDField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
