from django.db import models

from django_pgjson.fields import JsonField

from apps.common.models import *
from .mixins import Stripe

# Create your models here.

class BasePaymentModel(Stripe, TimeStamped):
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)
    attempts = models.IntegerField(default=0)

    #service charges
    service_charges = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)
    tax = models.DecimalField(default=0.0, max_digits=20, decimal_places=4)
    total_amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)

    # extra timestamps
    attempted_on = models.DateTimeField(blank=True, null=True)
    charged_on = models.DateTimeField(blank=True, null=True)

    gateway_response = JsonField(default={})
    is_paid = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Invoice(BasePaymentModel):
    company = models.ForeignKey('companies.Company', related_name='invoices')
    # FK relationships
