from .base import *

DEBUG = env.bool("DJANGO_DEBUG", False)

SECRET_KEY = env.str("DJANGO_SECRET_KEY")
DATABASES = {"default": env.db("DATABASE_URL")}
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
