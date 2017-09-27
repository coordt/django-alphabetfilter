import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# APP = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(APP)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g2_39yupn*6j4p*cg2%w643jiq-1n_annua*%i8+rq0dx9p=$n'


ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.abspath(os.path.join(PROJ_ROOT, 'templates')),
        ],
    },
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'alphafilter',
    'testtags',
)

ALPHAFILTER_ADMIN_FIELDS = {
    'auth.user': 'username',
    'auth.group': 'name',
}
