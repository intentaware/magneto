# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_invoice_gateway_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='tax',
            new_name='taxes',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='total_amount',
        ),
    ]
