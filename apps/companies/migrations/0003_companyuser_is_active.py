# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_companygroup_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyuser',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
