# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields

import shortuuid

def set_key(apps, schema_editor):
    Company = apps.get_model('companies', 'Company')

    for c in Company.objects.all():
        c.publisher_key = shortuuid.uuid()
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20150316_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='publisher_key',
            field=django_extensions.db.fields.ShortUUIDField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.RunPython(set_key),
    ]
