from .base import *

DEBUG = False

DB_STRING = env.str("DATABASE_URL", default=None)
DATABASES = {"default": env.db(DB_STRING)}

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
