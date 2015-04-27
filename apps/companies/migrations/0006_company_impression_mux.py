# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_company_publisher_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='impression_mux',
            field=models.IntegerField(default=1000),
            preserve_default=True,
        ),
    ]
