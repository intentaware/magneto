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
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('name', models.CharField(default=b'', max_length=256)),
                ('description', models.TextField(null=True, blank=True)),
                ('starts_on', models.DateTimeField(null=True, blank=True)),
                ('ends_on', models.DateTimeField(null=True, blank=True)),
                ('is_coupon_ad', models.BooleanField(default=False)),
                ('counter', models.BigIntegerField(default=0)),
                ('serve_limit', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
                ('c2a', models.URLField(verbose_name=b'Call to Action')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('code', django_extensions.db.fields.ShortUUIDField(editable=False, blank=True)),
                ('redeemed_on', models.DateTimeField(null=True, blank=True)),
                ('claimed_on', models.DateTimeField(null=True, blank=True)),
                ('campaign', models.ForeignKey(related_name='coupons', to='campaigns.Campaign')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
