import os
# from filebrowser.sites import site as fbsite

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = '/home/guest007/tmp/Projects/vyborg-gid/static/'
MEDIA_ROOT = '/home/guest007/tmp/Projects/vyborg-gid/media/'

# fbsite.directory = "images/"