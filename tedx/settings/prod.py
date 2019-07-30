from .base import *

DEBUG = False
ADMINS = (
    ('Mohammad Moallemi', 'mohammadmoallemi@outlook.com'),
)
ALLOWED_HOSTS = ['tedxui.ir', 'www.tedxui.ir', '45.82.136.179', ]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tedx',
        'USER': 'tedx',
        'PASSWORD': 'F|_|ll$tackD3V',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
