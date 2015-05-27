from rest_framework.exceptions import ValidationError
from django.utils import timezone


class StripeCardValidator(object):
    def __init__(self, klass, *args, **kwargs):
        self.message = None
        self.klass = klass

    def set_context(self, serializer):
        if type(self.klass) is str:
            self.klass = getattr(serializer, self.klass, None)

    def __call__(self, attrs):
        amount = attrs.pop('amount', None)
        import math
        cents, dollars = math.modf(amount)
        cents = (int(dollars) * 100) + int(cents * 100)
        print cents
        self.klass._params = {
            "source": attrs,
        }
        charge, response = self.klass.charge(amount_in_cents=cents,
            description='Invoice #%s' %(self.klass.id), currency='CAD')
        if charge:
            self.klass.charged_on = timezone.now()
            self.klass.is_paid = True
            self.klass.gateway_response = response
            self.klass.save()
        if not charge:
            raise ValidationError(response.message)
