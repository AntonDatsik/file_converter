from .apps import INSTALLED_APPS
from .auth_user import *
from .base import *
from .databases import DATABASES
from .logging import LOGGING
from .middlewares import MIDDLEWARE
from .rest_framework import REST_FRAMEWORK
from .templates import TEMPLATES

try:
    from settings_local import *
except ImportError:
    pass
