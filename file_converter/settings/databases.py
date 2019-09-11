import os

__all__ = (
    'DATABASES',
)

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('SQL_DATABASE', 'converter'),
            'USER': os.environ.get('SQL_USER', 'dev'),
            'HOST': os.environ.get('SQL_HOST', 'localhost'),
            'PORT': os.environ.get('SQL_PORT', '5432'),
            'PASSWORD': os.environ.get('SQL_PASSWORD', 'dev_password'),
        }
    }
