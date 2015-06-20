# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0017_auto_20150516_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='payment_data',
            field=django_pgjson.fields.JsonField(default={}),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companygroup',
            name='permissions',
            field=django_pgjson.fields.JsonField(default=[]),
            preserve_default=True,
        ),
    ]
