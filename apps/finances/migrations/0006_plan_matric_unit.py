# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='matric_unit',
            field=models.IntegerField(default=1),
        ),
    ]
