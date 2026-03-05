from .base import *

DEBUG = False

SECRET_KEY = "django-insecure-+v%5l=#_jw!@*e=&n7e!ov$4je6-_7j4bnq1f)x!3lkuawm3o5"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
