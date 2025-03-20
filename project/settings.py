import os
from dotenv import load_dotenv
from environs import env
load_dotenv()

DATABASE_NAME = env("NAME")
DATABASE_USER = env("USER")
DATABASE_PASSWORD = env("PASSWORD")
DATABASE_SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = DATABASE_SECRET_KEY

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
