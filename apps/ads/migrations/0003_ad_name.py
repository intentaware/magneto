# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20150225_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='name',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
    ]
