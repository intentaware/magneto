from django.db import models
from apps.common.models import *
from .mixins import Stripe

# Create your models here.

class BasePaymentModel(Stripe, TimeStamped):
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)
    attempts = models.IntegerField(default=0)

    # extra timestamps
    attempted_on = models.DateTimeField(blank=True, null=True)
    charged_on = models.DateTimeField(blank=True, null=True)

    is_paid = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Invoice(BasePaymentModel):
    company = models.ForeignKey('companies.Company', related_name='invoices')
    # FK relationships
