"""
WSGI config for pydjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_startup.settings")

application = get_wsgi_application()

"""
gunicorn -h

gunicorn [options] module_name:variable_name

cmd:
gunicorn -b 0.0.0.0:8888 -w 1 --threads 10 -k gevent module_name:app_name -D        # 单进程多线程
gunicorn -b 0.0.0.0:8000 -w 3 pydjango.wsgi:application -D                           # 多进程单线程
gunicorn -b 0.0.0.0:8000 -w 3 --threads 10 -k gevent pydjango.wsgi:application -D     # 多进程多线程
"""
