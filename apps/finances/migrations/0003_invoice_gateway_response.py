# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_tax_and_service_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='gateway_response',
            field=django_pgjson.fields.JsonField(default={}),
            preserve_default=True,
        ),
    ]
