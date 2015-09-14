# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0018_auto_20150516_2013'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companycircle',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='companycircle',
            name='circle',
        ),
        migrations.RemoveField(
            model_name='companycircle',
            name='company',
        ),
        migrations.RemoveField(
            model_name='company',
            name='circles',
        ),
        migrations.DeleteModel(
            name='CompanyCircle',
        ),
        migrations.DeleteModel(
            name='Circle',
        ),
    ]
