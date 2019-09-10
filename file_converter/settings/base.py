__all__ = (
    'ALLOWED_HOSTS',
    'BASE_DIR',
    'DEBUG',
    'ROOT_URLCONF',
    'SECRET_KEY',
    'TIME_ZONE',
    'WSGI_APPLICATION',
    'STATIC_URL',
    'STATIC_ROOT',
    'MEDIA_URL',
    'MEDIA_ROOT'
)


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+di%ttaxve0xmjx8lyerx%kk@k@8bbg2zss92*i2)in0^@(@*b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


ROOT_URLCONF = 'file_converter.urls'


SHOW_DOCS = True

WSGI_APPLICATION = 'file_converter.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
