"""
Production-ready deployment settings

"""
from project.project.defaults import *

# Choose which site we're using. initial_data.yaml installs some
# fixture data so that localhost:8000 has SIDE_ID == 1, and
# h4h.mst.edu has SITE_ID == 2
#
# Since we're deploying on h4h.mst.edu, SITE_ID should be 2.
SITE_ID = 2

# Since we're behind a proxy
USE_X_FORWARDED_HOST = True


##########################################################################
#
# Database
#
##########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSTGRES_DB,            # Should be in secret_settings.py
        'USER': POSTGRES_USER,          # Should be in secret_settings.py
        'PASSWORD': POSTGRES_PASSWORD,  # Should be in secret_settings.py
        'HOST': 'localhost'
    }
}

##########################################################################
#
# Templates
#
##########################################################################

# Debug templates
for t in TEMPLATES:
    t["OPTIONS"]["debug"] = False


##########################################################################
#
# Cache
#
##########################################################################

# CACHES = { }


##########################################################################
#
# Logging
#
##########################################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry', 'console', 'logfile'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
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
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },

        # Log all debug information for our apps to stdout and to a file
        'webserver': {
            'level': 'DEBUG',
            'handlers': ['console', 'logfile'],
            'propagate': True,
        },
        'competition': {
            'level': 'DEBUG',
            'handlers': ['console', 'logfile'],
            'propagate': True,
        }
    }
}
