# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_companyuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='compnay',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
