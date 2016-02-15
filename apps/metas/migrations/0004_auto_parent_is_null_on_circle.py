# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0003_model_publisher_cirlce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='parent',
            field=models.ForeignKey(related_name='children', blank=True, to='metas.Circle', null=True),
        ),
    ]
