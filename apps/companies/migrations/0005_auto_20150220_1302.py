# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_compnay_is_active'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companyuser',
            unique_together=set([('user', 'group', 'company')]),
        ),
    ]
