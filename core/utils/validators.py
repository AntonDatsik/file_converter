import re
from rest_framework.serializers import ValidationError
from django.utils.translation import gettext_lazy as _


class FileFieldValidator:
    EXTENSION_REGEX = re.compile(r'^.+\.(?P<extension>[a-z\d]+)$', flags=re.IGNORECASE)

    def __init__(self, extension):
        self.extension = extension.lower()

    def __call__(self, value):
        file_name = value.name
        match = self.EXTENSION_REGEX.match(file_name)
        if not match:
            raise ValidationError(_("File don't have extension."))
        extension = match.group('extension').lower()
        if extension != self.extension:
            raise ValidationError(
                _("File have wrong extension. %(exp_extension)s is expected, got %(extension)s.") % {
                    'exp_extension': self.extension,
                    'extension': extension
                }
            )
