import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "tests",
    'm1',
    'django.contrib.contenttypes',
]

ROOT_URLCONF = 'django_startup.urls'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "NAME": "django",
        "USER": "imake",
        "PASSWORD": "12315",
        "HOST": "tk",
        "PORT": "3306",
        'TEST': {
            'NAME': 'test_django',
        },
    }
}
