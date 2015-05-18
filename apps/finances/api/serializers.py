from rest_framework import serializers
from apps.finances.models import Invoice
from apps.api.serializers import StripeCreditCardSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice

class InvoiceChargeSerializer(StripeCreditCardSerializer):

    def clean(self):
        cleaned_data = super(StripeCreditCardSerializer, self).clean()
        #source = self.get_source(cleaned_data)
        s = Stripe()
        check, response = s.charge(cleaned_data['amount'], cleaned_data['description'], source=source)
        if not check:
            print response
            raise serializers.ValidationError(response.json_body)
        else:
            self.charge = response
