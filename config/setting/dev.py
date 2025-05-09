from ..settings import *

DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = []

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "node_modules",
]

MEDIA_ROOT = BASE_DIR / "media"
