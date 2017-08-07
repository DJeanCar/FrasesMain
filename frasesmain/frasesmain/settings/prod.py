from .base import *

DEBUG = False

ALLOWED_HOSTS = ['frasesdeamor.com.pe']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'frasesmain',
        'USER' : 'frasesmain',
        'PASSWORD' : 'frasesmain',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = 'http://frasesdeamor.com.pe/media/'

STATIC_ROOT = BASE_DIR.child('static')
MEDIA_ROOT = BASE_DIR.child('media')