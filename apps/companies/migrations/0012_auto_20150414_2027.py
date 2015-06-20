# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_populate_circles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circle',
            options={'ordering': ('name',)},
        ),
    ]
