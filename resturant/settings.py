"""
Django settings for resturant project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w*x(lmr%_f)rs*+)@i0t-981j_9+vaqt@d*58%y6$+10phv+6+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menu.apps.MenuConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'resturant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'resturant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


'''
# DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django_new',
        'USER': 'root',
        'PASSWORD': 'SolomonK@1',
        'HOST': 'my-resturant-website-project.onrender.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR, 'static'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'adminstatic')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
# title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Sol Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Sol Recipe",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Sol Recipe",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "../static/images/chef new 1.jpg",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "../static/images/Chef catoon.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": True,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "../static/images/chef 3.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Solomon Recipe",

    # Copyright on the footer
    "copyright": "Emmy Limited",
    
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.User": "fas fa-user",
        "menu": "fas fa-book",
        "menu.Menu": "fa fa-book",
        "menu.CartItem": "fa fa-id-badge",
        "menu.Cart": "fa fa-key",
    },
    
    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "/", 'name': 'home', 'url': 'home' },

        # model admin to link to (Permissions checked against model)
        {"model": "auth.user"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "auths"},
    ],

    
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/emmanuel-13", "new_window": True},
        {"model": "auth.User", "icons": "fas fa-user"}
     ],
}


PAYSTACK_SECRET_KEY ="sk_test_1ef5e3b82a4de898ed673d7e2561e026ab027b56"
PAYSTACK_PUBLIC_KEY ="pk_test_0a6061ba13ee31e6e6ae9df2654ed5e2f1c79f33"
