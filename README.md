# Django Registration

## Requirements

You need to install:

    $ virtualenv envRegistration
    $ source envRegistration/bin/activate
    $ pip install Django
    $ pip install -r requirements.txt

## Create DB

Inside project root:

    $ python manage.py migrate

## Create SuperUser

Inside project root:

    $ python manage.py createsuperuser

## Run Server

Inside project root:

    $ python manage.py runserver 

## Fabric utilities

We are using Fabric to install / deploy / help developers with rapid commands. This is an updated list of fabric commands:

| Option | Description |
| ------ | ----------- |
| **install**   | Used to install Django and project requirements |
| **migrate** | Used to create Databases and help with migration |
| **migrate_app** | Used to create a specific database given app-name |
| **create_admin** | Used to create new admin for the project |
| **start** | Used to run the server | 


