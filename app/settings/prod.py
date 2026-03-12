from .base import *

DEBUG = True

SECRET_KEY = env.str("DJANGO_SECRET_KEY")
DATABASES = {"default": env.db("DATABASE_URL")}

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
