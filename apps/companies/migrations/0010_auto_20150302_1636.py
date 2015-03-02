# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_companygroup_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companygroup',
            name='permissions',
            field=jsonfield.fields.JSONField(default=b'[]'),
            preserve_default=True,
        ),
    ]
