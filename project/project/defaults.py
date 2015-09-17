import os
from django.contrib import messages

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)
BUILDOUT_DIR = os.path.dirname(PROJECT_DIR)
VAR_DIR = os.path.join(BUILDOUT_DIR, "var")


##########################################################################
#
# Secret settings
#
##########################################################################
# If a secret_settings file isn't defined, open a new one and save a
# SECRET_KEY in it. Then import it. All passwords and other secret
# settings should be stored in secret_settings.py. NOT in settings.py
try:
    from secret_settings import *
except ImportError:
    print "Couldn't find secret_settings.py file. Creating a new one."
    secret_path = os.path.join(SETTINGS_DIR, "secret_settings.py")
    with open(secret_path, 'w') as secret_settings:
        secret_key = ''.join([chr(ord(x) % 90 + 33) for x in os.urandom(40)])
        secret_settings.write("SECRET_KEY = '''%s'''\n" % secret_key)
    from secret_settings import *


##########################################################################
#
#  Authentication settings
#
##########################################################################

# When a user successfully logs in, redirect here by default
LOGIN_REDIRECT_URL = '/'

# The address to redirect to when a user must authenticate
LOGIN_URL = '/accounts/google/login/?process=login'

ACCOUNT_SIGNUP_FORM_CLASS = 'project.profiles.forms.SignupForm'

# Require that users who are signing up provide an email address
ACCOUNT_EMAIL_REQUIRED = True

# Don't store login tokens. We don't need them.
SOCIALACCOUNT_STORE_TOKENS = False

# Try to pull username/email from provider.
SOCIALACCOUNT_AUTO_SIGNUP = False

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    },
}

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/profile/%s/" % u.username,
}


##########################################################################
#
# Email Settings
#
##########################################################################

# These should be added to secret_settings.py

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = ''
# EMAIL_PORT = 587
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = ''


##########################################################################
#
# API settings
#
##########################################################################

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


##########################################################################
#
# Bleach settings
#
##########################################################################
import bleach

ALLOWED_HTML_TAGS = bleach.ALLOWED_TAGS + ['h1', 'h2', 'h3', 'p', 'img']

ALLOWED_HTML_ATTRS = bleach.ALLOWED_ATTRIBUTES
ALLOWED_HTML_ATTRS.update({
    'img': ['src', 'alt'],
})


##########################################################################
#
# Crispy settings
#
##########################################################################

CRISPY_TEMPLATE_PACK = "bootstrap3"


##########################################################################
#
# Messages settings
#
##########################################################################

# Change the default messgae tags to play nice with Bootstrap
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


##########################################################################
#
# Database settings
#
##########################################################################

# Should be overridden by development.py or production.py
DATABASES = None


##########################################################################
#
# Location settings
#
##########################################################################

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True


##########################################################################
#
# Static files settings
#
##########################################################################
MEDIA_ROOT = os.path.join(VAR_DIR, "uploads")
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_DIR, "static")
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

COMPRESS_ENABLED = True

##########################################################################
#
# Template settings
#
##########################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, "templates")],
        'OPTIONS': {
            'context_processors': [
                # Django
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    },
]


##########################################################################
#
# Middleware settings
#
##########################################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


##########################################################################
#
# URL settings
#
##########################################################################

ROOT_URLCONF = 'project.project.urls'


##########################################################################
#
# Installed apps settings
#
##########################################################################

INSTALLED_APPS = (
    # Django Content types *must* be first.
    'django.contrib.contenttypes',

    # AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Admin Tools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Crispy Forms
    'crispy_forms',

    # Rest Framework
    'rest_framework',

    # Django Extensions
    'django_extensions',

    # Compressor
    'compressor',

    # H4H apps
    'project.teams',
    'project.profiles',

    # Sentry client
    'raven.contrib.django.raven_compat',
)
