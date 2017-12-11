# CRINGE FILE NAME ALERT(PC culture is not even rational)
import sys

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'autogger',
        'USER': 'postgres_user',
        'PASSWORD': 'postgres_user_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_autogger',
        'USER': 'postgres_user',
        'PASSWORD': 'postgres_user_password',
        'HOST': 'localhost',
    }
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=core,jira,github,user',
    '--cover-html',
    '--cover-erase'
]

ALLOWED_HOSTS = ['localhost', ]
ROOT_SITE_DOMAIN = 'http://localhost:8090/'

DJANGO_ADMIN_SUPER_USER_EMAIL = 'john-doe@example.com'
DJANGO_ADMIN_SUPER_USER_PASSWORD = 'EXAMPLE_PASSWORD'
