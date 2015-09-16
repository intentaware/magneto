# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0003_model_publisher_cirlce'),
        ('companies', '0019_auto_20150914_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='circles',
            field=models.ManyToManyField(to='metas.Circle', through='metas.PublisherCircle'),
        ),
    ]
