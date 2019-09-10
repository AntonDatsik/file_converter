import os

from .apps import INSTALLED_APPS
from .auth_user import *
from .base import *
from .databases import DATABASES
from .middlewares import MIDDLEWARE
from .templates import TEMPLATES
from .rest_framework import REST_FRAMEWORK
from .logging import LOGGING


settings_local = os.environ.get(
    'PDF_GENERATOR_SETTINGS_LOCAL_PATH',
    os.path.join(BASE_DIR, 'settings_local.py'),
)

if os.path.exists(settings_local):
    exec(open(settings_local).read())
