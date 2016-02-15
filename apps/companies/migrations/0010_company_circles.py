# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20150414_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='circles',
            field=models.ManyToManyField(to='companies.Circle', through='companies.CompanyCircle'),
            preserve_default=True,
        ),
    ]
