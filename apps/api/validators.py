from rest_framework.exceptions import ValidationError
from django.utils import timezone


class StripeCardValidator(object):
    '''
    A stripe credit card validator
    '''
    def __init__(self, klass, *args, **kwargs):
        '''
        the initializing requires a serializer upon which the validator
        is being set

        Params:
            klass - defines the serializer upon which the class
        '''
        self.message = None
        self.klass = klass

    def set_context(self, serializer):
        if type(self.klass) is str:
            self.klass = getattr(serializer, self.klass, None)

    def __call__(self, attrs):
        amount = attrs.pop('amount', None)
        import math
        cents, dollars = math.modf(amount)
        # why am i multiplying cents by 100, need to check
        # with what am i sending from frontend?
        cents = (int(dollars) * 100) + int(cents * 100)
        print cents
        self.klass._params = {
            "source": attrs,
        }
        # why is the currency hard coded here?
        charge, response = self.klass.charge(amount_in_cents=cents,
            description='Invoice #%s' %(self.klass.id), currency='CAD')
        if charge:
            self.klass.charged_on = timezone.now()
            self.klass.is_paid = True
            self.klass.gateway_response = response
            self.klass.save()
        if not charge:
            raise ValidationError(response.message)
