from decouple import config
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a95%n8j8mo@j(!=!h%9@246)+@n1evte*g47v40wo)5@4=gbv('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'security',  # Custom security app
    'rosetta',  # For translation management
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Added for language support
    'django.middleware.locale.LocaleMiddleware',
    # 'security.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tshaweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],  # Directory for templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom context processor for user data
                'security.context_processor.show_data',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'tshaweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/


TIME_ZONE = 'UTC'

# USE_I18N = True
# LANGUAGE_CODE = 'en-us'


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom settings for the application
GRAPPELLI_ADMIN_TITLE = "Stemgon Inc"

PAYFAST_MERCHANT_KEY = config("PAYFAST_MERCHANT_KEY")
PAYFAST_MERCHANT_ID = config("PAYFAST_MERCHANT_ID")
PAYFAST_SANDBOX_MERCHANT_ID = config("PAYFAST_SANDBOX_MERCHANT_ID")
PAYFAST_SANDBOX_MERCHANT_KEY = config("PAYFAST_SANDBOX_MERCHANT_KEY")


MEDIA_ROOT='/home/miammnsf/tshapfutshesda/media'
STATIC_ROOT='/home/miammnsf/tshapfutshesda/static'# STATIC_ROOT = BASE_DIR / 'assets'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Directory for static files
]   


LANGUAGE_CODE = 'en'

USE_I18N = True

LANGUAGES = [
    ('en', _('English')),
    ('de', _('Tshivenda')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

AUTH_USER_MODEL = 'security.User'  # Custom user model
LOGIN_URL = '/login/'  # Redirect to login page if not authenticated

GRAPPELLI_ADMIN_TITLE = "Stemgon Inc"

PAYFAST_MERCHANT_KEY = config("PAYFAST_MERCHANT_KEY")
PAYFAST_MERCHANT_ID = config("PAYFAST_MERCHANT_ID")
PAYPAL_CLIENT_ID = config("PAYPAL_CLIENT_ID")
PAYFAST_SANDBOX_MERCHANT_ID = config("PAYFAST_SANDBOX_MERCHANT_ID")
PAYFAST_SANDBOX_MERCHANT_KEY = config("PAYFAST_SANDBOX_MERCHANT_KEY")

JAZZMIN_SETTINGS = {
  
    "site_logo": "img/favicon.png",
     "site_title": "Tshafutshe Admin Portal",
    "site_header": "Tshafutshe Dashboard",
    "site_brand": "Tshafutshe SDA",
    "welcome_sign": "Welcome to Tshafutshe Admin",
    "copyright": "Tshafutshe SDA Church",
    "search_model": "security.User",
}

LOGOUT_REDIRECT_URL = '/admin/login/'
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'
CSRF_TRUSTED_ORIGINS = ["https://stemgon.co.za", "https://www.stemgon.co.za", "https://*.ngrok-free.app"]
