from .base import *

DEBUG = True

DATABASES = {"default": env.db("DATABASE_URL")}

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
