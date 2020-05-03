import os
import dj_database_url

from toroto_challenge.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

# Update database configuration with $DATABASE_URL.
DATABASES['default'] = dj_database_url.config(conn_max_age=500)


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ['https://secret-shelf-40223.herokuapp.com/']

INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

# Configuration for whitenoise
# MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, '/assets/')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'assets'),
# )

# STATIC_ROOT = os.path.join(BASE_DIR, '/assets/')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '../front/src/assets/'),
# )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "../", "frontend", "build")]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "../", "frontend", "build", "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
WHITENOISE_ROOT = os.path.join(BASE_DIR, "../", "frontend", "build", "root")