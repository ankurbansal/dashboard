"""
Django settings for dashboard project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

os.environ.setdefault("LC_ALL","en_US.UTF-8 ")
# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control. Consider loading
# the secret key from an environment variable or a file instead.
SECRET_KEY = '5jsaex_6xyl#)g(m+iqhr*w1!6yu6p3rna1gp&bqi1-x3i)w7r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'tooling'
)




MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dashboard.urls'

WSGI_APPLICATION = 'dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'dashboard' ,
#        'HOST': '127.0.0.1' ,
#        'PORT': '3306' ,
#        'USER': 'root' ,
#        'PASSWORD': 'sakshi'
        'NAME': r'C:/Users/sakjain/Desktop/workspace/dashboard/resources/dashboard.db',# Or path to database file if using sqlite3.
        'USER': 'admin',# Not used with sqlite3.
        'PASSWORD': 'admin',# Not used with sqlite3.
        'HOST': 'admin',# Set to empty string for localhost. Not used with sqlite3.
        'PORT': 'admin',# Set to empty string for default. Not used with sqlite3.
    }
#             ,
#    'builds': {
#        'NAME': 'user_data',
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': 'mysql_user',
#        'PASSWORD': 'superS3cret'
#    },
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS=(
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "C:/Users/sakjain/Desktop/workspace/dashboard/templates/",
    
)
