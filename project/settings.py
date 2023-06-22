import os
from pathlib import Path
import environ
from django.template.context_processors import static

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    ACCOUNT_DEFAULT_HTTP_PROTOCOL=(str, 'https'),
    EMAIL_BACKEND=(str, 'EMAIL_BACKEND'),
)
environ.Env.read_env(os.path.join(BASE_DIR / 'project/.env.example'))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env('DEBUG')
ALLOWED_HOSTS: list[str] = env('ALLOWED_HOSTS')

INSTALLED_APPS = [
    # DJANGO_APPS
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # THIRD_PARTY_APPS
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    'django_extensions',
    # LOCAL_APPS
    "dailyInbox.accounts",
    "dailyInbox.core",
    'dailyInbox.entries',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Authentication
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
EMAIL_BACKEND = env("EMAIL_BACKEND")
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ACCOUNT_ADAPTER = default
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = default
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = default
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = default
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = default
# ACCOUNT_EMAIL_CONFIRMATION_HMAC = default
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'EmailService'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = env('ACCOUNT_DEFAULT_HTTP_PROTOCOL')
# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = default
# ACCOUNT_EMAIL_MAX_LENGTH = default
# ACCOUNT_MAX_EMAIL_ADDRESSES = default
# ACCOUNT_FORMS = default
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = default
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = default
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# ACCOUNT_LOGOUT_ON_GET = default
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = default
# ACCOUNT_LOGIN_ON_PASSWORD_RESET = default
# ACCOUNT_LOGOUT_REDIRECT_URL = default
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = default
ACCOUNT_PRESERVE_USERNAME_CASING = False
# ACCOUNT_PREVENT_ENUMERATION = default
# ACCOUNT_RATE_LIMITS = default
ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = default
# ACCOUNT_SIGNUP_FORM_CLASS = default
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_SIGNUP_REDIRECT_URL = default
# ACCOUNT_TEMPLATE_EXTENSION = default
# ACCOUNT_USERNAME_BLACKLIST = default
# ACCOUNT_UNIQUE_EMAIL = default
ACCOUNT_USER_DISPLAY = lambda user: user.email
# ACCOUNT_USER_MODEL_EMAIL_FIELD = default
# ACCOUNT_USER_MODEL_USERNAME_FIELD = default
# ACCOUNT_USERNAME_MIN_LENGTH = default
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USERNAME_VALIDATORS = default
# SOCIAL_ACCOUNT_* = default


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATICFILES_STORAGE = ''

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django-extensions
GRAPH_MODELS = {
    'app_labels': ["accounts", "core"],
    "rankdir": "BT",
    "output": "models.png"
}
