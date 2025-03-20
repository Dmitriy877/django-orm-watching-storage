import os
from dotenv import load_dotenv
from environs import env
load_dotenv()

DATABES_NAME = env("NAME")
DATABES_USER = env("USER")
DATABES_PASSWORD = env("PASSWORD")
DATABES_SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)

print(DEBUG)
print(type(DEBUG))

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'HOST': 'checkpoint.devman.org',
#         'PORT': '5434',
#         'NAME': DATABES_NAME,
#         'USER': DATABES_USER,
#         'PASSWORD': DATABES_PASSWORD,
#     }
# }

# INSTALLED_APPS = ['datacenter']

# SECRET_KEY = DATABES_SECRET_KEY

# ROOT_URLCONF = 'project.urls'

# ALLOWED_HOSTS = ['*']


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#     },
# ]


# USE_L10N = True

# LANGUAGE_CODE = 'ru-ru'

# TIME_ZONE = 'Europe/Moscow'

# USE_TZ = True

# DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
