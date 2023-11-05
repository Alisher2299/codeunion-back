from typing import Tuple

DJANGO_APPS: Tuple[str, ...] = (
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sessions",
)
SIDE_APPS: Tuple[str, ...] = (
    'corsheaders',
    'rest_framework',
    "rest_framework_simplejwt.token_blacklist",
    'django_extensions',
    'django_filters',
    'storages',
)
PROJECT_APPS: Tuple[str, ...] = (
    "common.apps.CommonConfig",
    "currencies.apps.CurrenciesConfig",
    "users.apps.UsersConfig",
)
DEFAULT_APPS: Tuple[str, ...] = DJANGO_APPS + SIDE_APPS + PROJECT_APPS
