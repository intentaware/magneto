# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_ad_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='compnay',
            new_name='company',
        ),
        migrations.AddField(
            model_name='ad',
            name='c2a',
            field=models.URLField(default=1, verbose_name=b'Call to Action'),
            preserve_default=False,
        ),
    ]
