# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_company_impression_mux'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='impression_mux',
        ),
        migrations.AddField(
            model_name='company',
            name='impressions_per_dollar',
            field=models.IntegerField(default=1000, help_text=b'No. of impressions generated against each USD'),
            preserve_default=True,
        ),
    ]
