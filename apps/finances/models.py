from django.db import models
from apps.common.models import *
from .mixins import Stripe

# Create your models here.

class BaseInvoice(Stripe, TimeStamped):

    class Meta:
        abstract = True
