
from base import *

DEBUG = os.environ['DEBUG']

# Enable security for website
# Force HTTPS
SECURE_SSL_REDIRECT = True # [1]

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

