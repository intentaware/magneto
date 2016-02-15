# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0014_impression_user_to_visitor'),
        ('users', '0005_visitor')
    ]

    operations = [
        migrations.AlterField(
            model_name='impression',
            name='visitor',
            field=models.ForeignKey(related_name='impressions', to='users.Visitor'),
        )
    ]
