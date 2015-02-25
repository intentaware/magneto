# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('starts_on', models.DateTimeField(null=True, blank=True)),
                ('ends_on', models.DateTimeField(null=True, blank=True)),
                ('counter', models.BigIntegerField(default=0)),
                ('serve_limit', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
