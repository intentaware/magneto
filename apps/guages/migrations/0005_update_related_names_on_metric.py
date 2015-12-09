# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guages', '0004_rename_matric_metric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='asset',
            field=models.ForeignKey(related_name='metrics', to='guages.Asset'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='visitor',
            field=models.ForeignKey(related_name='metrics', to='users.Visitor'),
        ),
    ]
