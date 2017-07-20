
from base import *

DEBUG = True

# Enable security for website
# Force HTTPS
SECURE_SSL_REDIRECT = False # [1]

# Get local environment
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']

# Set local database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'PORT': '',
    }
}


