# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_company_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='companygroup',
            name='name',
            field=models.CharField(default='Administrators', max_length=128),
            preserve_default=False,
        ),
    ]
