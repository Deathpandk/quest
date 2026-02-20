from .base import BASE_DIR

DEBUG = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

COV_ROOT = BASE_DIR / "htmlcov"
COV_URL = "coverage"
