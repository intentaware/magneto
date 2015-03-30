# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_company_publisher_key'),
        ('impressions', '0004_auto_20150329_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impression',
            old_name='data',
            new_name='meta',
        ),
        migrations.AddField(
            model_name='impression',
            name='pubisher',
            field=models.ForeignKey(related_name='impressions', default=1, to='companies.Company'),
            preserve_default=False,
        ),
    ]
