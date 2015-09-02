"""
Development settings

WARNING: These settings are NOT suitable for production.

"""
import project.project.defaults as default_settings
from project.project.defaults import *

# Choose which site we're using. initial_data.yaml installs some
# fixture data so that localhost:8000 has SIDE_ID == 1, and
# h4h.mst.edu has SITE_ID == 2
#
# Since we're debugging, we want to keep the site at #1
SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["localhost:8000"]


##########################################################################
#
# Database
#
##########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, "db", "project.db"),
    }
}

##########################################################################
#
# Django Debug Toolbar
#
##########################################################################
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE_CLASSES = default_settings.MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = default_settings.INSTALLED_APPS + (
    'debug_toolbar',
)


##########################################################################
#
# Logging
#
##########################################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(VAR_DIR, "logs", "log.txt"),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'webserver': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        }
    }
}
