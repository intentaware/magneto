import base64
import imghdr
import uuid
import sys
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import ReadOnlyField, ImageField


DEFAULT_CONTENT_TYPE = "application/octet-stream"
ALLOWED_IMAGE_TYPES = (
    "jpeg",
    "jpg",
    "png",
    "gif"
)

EMPTY_VALUES = (None, '', [], (), {})


if sys.version_info.major == 3:
    string_type = str
else:
    string_type = basestring


class Base64ImageField(ImageField):
    """
    A django-rest-framework field for handling image-uploads through raw post data.
    It uses base64 for en-/decoding the contents of the file.
    """
    def to_internal_value(self, base64_data):
        # Check if this is a base64 string
        if base64_data in EMPTY_VALUES:
            return None

        if isinstance(base64_data, string_type):
            # Try to decode the file. Return validation error if it fails.
            frmt, b64_data = base64_data.split(';base64,')
            # print frmt
            # print b64_data
            try:
                decoded_file = base64.b64decode(b64_data)
            except TypeError:
                raise ValidationError(_("Please upload a valid image."))
            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)
            if file_extension not in ALLOWED_IMAGE_TYPES:
                raise ValidationError(_("The type of the image couldn't been determined."))
            complete_file_name = file_name + "." + file_extension
            data = ContentFile(decoded_file, name=complete_file_name)
            return super(Base64ImageField, self).to_internal_value(data)
        raise ValidationError(_('This is not an base64 string'))

    def to_representation(self, value):
        # Return url including domain name.
        return value.name

    def get_file_extension(self, filename, decoded_file):
        extension = imghdr.what(filename, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension


class ModelMethodField(ReadOnlyField):
    """
    A field that calls the method of the serialized object
    """
    def __init__(self, method_name=None, *args, **kwargs):
        self._method_name = method_name
        super(ModelMethodField, self).__init__(*args, **kwargs)

    def field_to_native(self, obj, field_name):
        return getattr(obj, self._method_name or field_name)()


class ModelPropertyField(ReadOnlyField):
    """
    A field that retrieves a custom property of the serialized object

    Useful for model functions using the @property decorator
    """
    def field_to_native(self, obj, field_name):
        return getattr(obj, field_name)
