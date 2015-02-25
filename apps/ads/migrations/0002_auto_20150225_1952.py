# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_company_users'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='title',
        ),
        migrations.AddField(
            model_name='ad',
            name='compnay',
            field=models.ForeignKey(related_name='ads', blank=True, to='companies.Company', null=True),
            preserve_default=True,
        ),
    ]
