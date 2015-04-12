from django.template import Library
from django.utils.safestring import mark_safe
import json

register = Library()

def jsonify(value):
    """
    Takes a python dictionary or list and returns a json,
    not to be used against querysets or complex dictionaries with
    python class objects
    """
    return json.dumps(value)

register.filter('jsonify', jsonify)
jsonify.is_safe = True
