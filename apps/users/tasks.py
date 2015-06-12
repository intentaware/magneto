from __future__ import absolute_import
from adomattic.celery import app as capp

@capp.task
def send_templated_email(receivers, template, context, **kwargs):
    """
    Sends a rendered email and send the email as an html,
    requires a template path and template context to be sent
    """
    from django.template.loader import render_to_string
    from django.core.mail import EmailMessage
    from django.conf import settings

    message = render_to_string(template, context)
    email = EmailMessage(
                to=[receivers,],
                from_email=settings.ADOMATTIC_FROM,
                body=message,
                **kwargs
            )
    email.content_subtype = 'html'
    email.send()
    return
