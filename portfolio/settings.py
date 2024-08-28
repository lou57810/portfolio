import os
import sentry_sdk
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
dsn = os.getenv('dsn')


sentry_sdk.init(
    # dsn="https://7b8fdb1a47491b415857d2e63a0c98b1@o4506869492940800.ingest.us.sentry.io/4507664861560832",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    dsn,
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-1_*8(#4bji4sj01d$%udblmym+g2qlvfuw3fmw5(ezjyj6@*dm'
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')
# DEBUG = DEBUG.lower() in ('true', '1', 'yes', 'on')
print('debug:', DEBUG)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'authentication',
    'blogapi',
]

WHITENOISE_MANIFEST_STRICT = False  # Pour éviter l'erreur pytest : missing staticfiles manifest entry

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'authentication.Subscriber'
ROOT_URLCONF = 'portfolio.urls'
"""
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'authentication', 'templates'),
            os.path.join(BASE_DIR, 'blogapi', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'portfolio.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'authentication.validators.ContainsLetterValidator',
    },
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# STATIC_URL = '/staticfiles/'
# STATICFILES_DIRS = [BASE_DIR.joinpath('static/')]
# STATICFILES_DIRS = [BASE_DIR.joinpath('staticfiles/')]
# STATIC_ROOT = os.path.join(BASE_DIR / 'staticfiles')
# STATIC_ROOT = os.path.join(BASE_DIR / 'static')

# LOGIN_URL = 'login'

# Apres login redirection sur home
LOGIN_REDIRECT_URL = 'home'
# Default primary key field type
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR / 'staticfiles')
STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / "static", ]
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-fields
MEDIA_URL = '/media/'   # images téléchargées par les utilisateurs loggés
MEDIA_ROOT = BASE_DIR.joinpath('media/')
# MEDIA_ROOT = os.path.join(BASE_DIR / 'media')
# MEDIA_ROOT = '/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
"""MEDIA_URL est l'URL depuis laquelle Django va essayer de servir des medias.
    MEDIA_ROOT indique le répertoire local dans lequel seront sauvegardées les
    images téléversées."""
