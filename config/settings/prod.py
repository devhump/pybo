from .base import *

ALLOWED_HOSTS = ['52.78.87.114']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'NnzKOH=F4:_+(Y>yCa1U#,I(j)5$VQ*L',
        'HOST': 'ls-38d0f7123dfc4d8791ada71af6288110bce300b1.cbcyaxpi6ofq.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}