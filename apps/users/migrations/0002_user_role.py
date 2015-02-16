# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='pb', max_length=2, choices=[(b'ar', b'ADVERTISER'), (b'pb', b'PUBLISHER')]),
            preserve_default=False,
        ),
    ]
