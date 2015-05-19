from rest_framework.exceptions import ValidationError


class StripeCardValidator(object):
    def __init__(self, klass, *args, **kwargs):
        self.message = None
        self.klass = klass

    def set_context(self, serializer):
        self.klass = getattr(serializer, self.klass, None)

    def __call__(self, attrs):
        amount = attrs.pop('amount', None)
        import math
        cents, dollars = math.modf(amount)
        cents = (int(dollars) * 100) + int(cents)
        print cents
        self.klass._params = {
            "source": attrs,
        }
        charge, response = self.klass.charge(amount_in_cents=cents,
            description='Invoice #%s' %(self.klass.id), currency='CAD')
        if not charge:
            raise ValidationError(response.message)
