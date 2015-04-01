# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('impressions', '0003_auto_20150310_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpressionUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('key', django_extensions.db.fields.ShortUUIDField(editable=False, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='impression',
            old_name='ad',
            new_name='campaign',
        ),
        migrations.AlterField(
            model_name='impression',
            name='user',
            field=models.ForeignKey(related_name='impressions', to='impressions.ImpressionUser'),
            preserve_default=True,
        ),
    ]
