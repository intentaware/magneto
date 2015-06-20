# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0006_auto_20141028_2005'),
        ('campaigns', '0003_auto_20150310_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='image',
            field=models.ForeignKey(related_name='campaigns', blank=True, to='photologue.Photo', null=True),
            preserve_default=True,
        ),
    ]
