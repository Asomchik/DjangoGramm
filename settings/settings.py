"""
Django settings for djangogramm project.

"""
import os
from pathlib import Path

from dotenv import load_dotenv
import django_heroku


# Load secret info to environment
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY_VALUE')
DEBUG = os.getenv('DEBUG_VALUE') == 'True'

ALLOWED_HOSTS = ['asomchik.herokuapp.com']

# Register custom User Model
AUTH_USER_MODEL = 'user.User'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.user',
    'apps.post',
    'apps.comment',
    'apps.chat',

    'easy_thumbnails',
    'debug_toolbar',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'urls.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static_collect'

# Media settings
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

# Default page for @login_required()
LOGIN_URL = 'login'

# Aliases preset for thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'avatar_big': {'size': (100, 100)},
        'avatar_medium': {'size': (60, 60)},
        'avatar_small': {'size': (40, 40)},
        'content_medium': {'size': (600, 600)},
        'content_small': {'size': (300, 300)},
    },
}

# For debug_toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]
# DB settings for Heroku
django_heroku.settings(locals())

# External storage for media_files
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME_VALUE'),
    'API_KEY': os.getenv('API_KEY_VALUE'),
    'API_SECRET': os.getenv('API_SECRET_VALUE'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'
THUMBNAIL_DEFAULT_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Email settings
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER_VALUE')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD_VALUE')

# Pagination settings
POSTS_PAGINATE_BY = 4
MESSAGES_PAGINATE_BY = 6

