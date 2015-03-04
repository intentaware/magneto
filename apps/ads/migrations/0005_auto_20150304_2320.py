# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0004_auto_20150301_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('code', django_extensions.db.fields.ShortUUIDField(editable=False, blank=True)),
                ('redeemed_on', models.DateTimeField(null=True, blank=True)),
                ('claimed_on', models.DateTimeField(null=True, blank=True)),
                ('ad', models.ForeignKey(related_name='coupons', to='ads.Ad')),
                ('claimed_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ad',
            name='is_coupon_ad',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
