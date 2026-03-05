from .base import BASE_DIR

DEBUG = True

SECRET_KEY = "django-insecure-+v%5l=#_jw!@*e=&n7e!ov$4je6-_7j4bnq1f)x!3lkuawm3o5"

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CORS_ALLOW_CREDENTIALS = TrueCORS_ALLOW_CREDENTIALS = True
# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

COV_ROOT = BASE_DIR / "htmlcov"
COV_URL = "coverage"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
