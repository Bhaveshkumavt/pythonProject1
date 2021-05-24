
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
# MEDIA_ROOT=os.path.join(BASE_DIR,'app1/media')                         #from ecomstore sattings.py

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1frk6ew5yp30v(+szx!_5&#a@bnk6)+=289yd^5ho2v7+oj_^*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# AUTH_REMEMBER_COOKIE_NAME = 'remember_token'                #for remember-me
# AUTH_REMEMBER_COOKIE_AGE = 86400 * 28  # 4 weeks by default #for remember-me
SESSION_COOKIE_AGE=60*60*24*30        #from ecomstore

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True                      #for rememebre
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'app1',
    'registration',
    'crispy_forms',
    'allauth',
    'allauth.account',
]                           #'auth_remember'



# AUTH_USER_MODEL='app1.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'auth_remember.middleware.AuthRememberMiddleware', # for remmeber-me functionality
]

MESSAGE_STORAGE='django.contrib.messages.storage.cookie.CookieStorage'  #from ecomstore

ROOT_URLCONF = 'website4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'website4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website4',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
        'OPTIONS':{
            'sql_mode':'traditional',
        }
    }
}

PASSWORD_HASSER=[
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_URL='/media/'
# IMAGEFILES_DIRS=[
#     IMAGE_DIR,
# ]

from django.urls import reverse_lazy                #from ecomstore sattings.py
LOGIN_SUCCESS_URL=reverse_lazy('profile')            #from ecomstore sattings.py

LOGIN_URL='app1/user_login'                     #from ecomstore sattings.py

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

ACCOUNT_ACTIVATION_DAYS = 3

DEFAULT_FROM_EMAIL = 'My Domain <noreply@mydomain.com>'          #from ecomstore sattings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'    #from ecomstore sattings.py
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'Kk1234@567&kajal'
EMAIL_HOST_USER = 'kajalkumavat27@gmail.COM'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS=[                                               #from ecomstore sattings.py
    'django.contrib.auth.backends.ModelBackend',                       #from ecomstore sattings.py
    # 'website4.auth.CustomEmailAuthBackend.EmailAuthBackend',         #from ecomstore sattings.py
    'allauth.account.auth_backends.AuthenticationBackend',              #from ecomstore sattings.py
    # 'auth_remember.backend.AuthRememberBackend',                   #for remember - me functionality
]

LOGIN_REDIRECT_URL = '/app1/login/'
SITE_ID=1                                                                #from ecomstore sattings.py

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = PROJECT_ROOT + '/static/'
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


ACCOUNT_EMAIL_REQUIRED = True                                #from ecomstore sattings.py
ACCOUNT_USERNAME_REQUIRED = True                             #from ecomstore sattings.py
