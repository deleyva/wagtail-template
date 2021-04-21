"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

"""

from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
if os.environ.get("DEBUG") is None or eval(os.environ.get("DEBUG")):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_conf.settings.dev")
elif not eval(os.environ.get("DEBUG")):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_conf.settings.production")

# you change change the name here
app = Celery("project_conf")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, count_hompage.s("hello"), name="Printing hello")

    # Calls print('world') every 30 seconds
    sender.add_periodic_task(30.0, print("world"), expires=10)


@app.task
def add(x, y):
    return x / y