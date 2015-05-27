from rest_framework import serializers
from apps.finances.models import Invoice
from apps.api.serializers import StripeCreditCardSerializer
from apps.api.validators import StripeCardValidator


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice

class InvoiceChargeSerializer(StripeCreditCardSerializer):
    class Meta:
        validators = [StripeCardValidator(klass='invoice'), ]
