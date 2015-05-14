import stripe
from django.conf import settings

class Stripe(object):
    """
    class to instantiate stripe and provide methods for error handling
    """

    def __init__(self, *args, **kwargs):
        stripe.api_key = settings.STRIPE_KEY
        self._stripe = stripe
        # params is a dictionary used to set parameters during a charge life
        # cycle, mostly used in post_save and pre_save methods
        self._params = dict()

    def pre_charge(self, *args, **kwargs):
        """
        to perform before preparing a charge,
        used to set self._params parameter
        """
        pass

    def charge(self, amount_in_cents, description, currency=None, *args, **kwargs):
        self.pre_charge(*args, **kwargs)
        if not currency:
            currency = 'CAD'
        try:
            self._params = self._stripe.Charge.create(
                amount=amount_in_cents,
                currency=currency,
                description=description,
                **self._params
            )
            self.post_charge(*args, **kwargs)
            return True, self._params
        except self._stripe.error.CardError, ce:
            self._params = ce
            return False, self._params

    def post_charge(self, *args, **kwargs):
        """
        to perform after the charge
        """
        pass
