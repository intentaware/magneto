# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_pgjson.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_visitor'),
        ('guages', '0003_auto_20151202_1534'),
    ]

    operations = [
        migrations.RenameModel('Matric', 'Metric')
    ]
