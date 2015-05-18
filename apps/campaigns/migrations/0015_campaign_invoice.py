# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
        ('campaigns', '0014_campaigncircle'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='invoice',
            field=models.ForeignKey(related_name='campaigns', blank=True, to='finances.Invoice', null=True),
            preserve_default=True,
        ),
    ]
