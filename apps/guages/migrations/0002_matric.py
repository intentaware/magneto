# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_pgjson.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_visitor'),
        ('guages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('meta', django_pgjson.fields.JsonBField()),
                ('asset', models.ForeignKey(related_name='matrices', to='guages.Asset')),
                ('visitor', models.ForeignKey(related_name='matrics', to='users.Visitor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
