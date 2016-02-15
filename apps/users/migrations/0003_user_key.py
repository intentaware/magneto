# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150310_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='key',
            field=django_extensions.db.fields.ShortUUIDField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
