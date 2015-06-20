# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('name', models.CharField(max_length=256)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'name', editable=False, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('permissions', jsonfield.fields.JSONField(default=b'[]')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('is_owner', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_default', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=32, null=True, blank=True)),
                ('company', models.ForeignKey(related_name='memberships', to='companies.Company')),
                ('group', models.ForeignKey(related_name='memberships', to='companies.CompanyGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
