import stripe
from django.conf import settings

class Stripe(object):
    """
    class to instantiate stripe and provide methods for error handling
    """

    def __init__(*args, **kwargs):
        stripe.api_key = settings.STRIPE_KEY
        self._stripe = stripe
        # params is a dictionary used to set parameters during a charge life
        # cycle, mostly used in post_save and pre_save methods
        self._params = Dict()

    def pre_charge(*args, **kwargs):
        """
        to perform before preparing a charge,
        used to set self._params parameter
        """
        pass

    def charge(self, amount_in_cents, currency, description, *args, **kwargs):
        self.pre_charge(*args, **kwargs)
        try:
            response = self._stripe.Charge.create(
                amount=amount_in_cents,
                currency='CAD',
                description=description,
                self._params,
            )
            self.post_charge(*args, **kwargs)
            return self._params = True, response
        except self._stripe.error.CardError, ce:
            return self._params = False, ce

    def post_charge(**args, **kwargs):
        """
        to perform after the charge
        """
        pass
