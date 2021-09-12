# My first time with Celery [Django]

This is a snippet code used to explain how Celery works integrate in Django Framework. 

You can check out the meetup recording on Youtube [here](https://youtu.be/L10-vyWvnMg)

# Set up from Zero

For this snippet code was used Django REST Framework: https://www.django-rest-framework.org/tutorial/quickstart/

1. Install Django REST Framework 

        pip install djangorestframework

2. Create the tutorial project

        django-admin startproject quickstart

3. Create the quickstart app

        django-admin startapp quickstart

4. Create a super user 

        python manage.py createsuperuser --email admin@example.com --username admin

> **NOTE:** You need to have an AWS account for send emails using AWS SES. You can set your AWS credentials using AWS CLI, environment variables or directly on boto3 client. 

Check out for variables with CELERY prefix in settings.py file to find broker connection settings and other things.

Magic occurrs because of tasks.py file in each app module.

# Execute current code in this repo

- Start REST API

        python manage.py runserver

- Start celery workers

        celery -A tutorial worker -l INFO