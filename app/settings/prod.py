import dj_database_url

from .base import *

DEBUG = False

DB_STRING = env.str("DATABASE_URL", default=None)
DATABASES = {"default": dj_database_url.parse(DB_STRING)}
