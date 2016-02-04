from __future__ import with_statement
from datetime import datetime
from fabric.api import *
import contextlib

def install():
    local('pip install Django')
    local('pip install -r requirements.txt')

def migrate():
    local('python manage.py migrate')

#fab migrate_app:'APP-NAME'
def migrate_app(app_name):
    local('python manage.py makemigrations %s' % app_name)

def create_admin():
    local('python manage.py createsuperuser')

def start():
    local('python manage.py runserver 0.0.0.0:8000')

