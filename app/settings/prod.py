from .base import *

DEBUG = False

DATABASES = {"default": env.db("DATABASE_URL")}

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
