from registration.signals import *


def registeration_signal(sender, **kwargs):
    user = kwargs['user']
    user.send_registration_email()

user_registered.connect(registeration_signal)
