# Podium #

Podium is an application for booking and scheduling talks for meetups.  This
app is being maintained by Python Atlanta Jam Session members to help schedule
 talks for our Python Atlanta meetups.

Python Atlanta's Podium is currently running at
https://pyatl-podium.herokuapp.com/

## Requirements ##
- Python 3.6+
- Django 1.11 - Base web framework
- Gunicorn 19.7.1 - WSGI webserver
- PostgreSQL - database engine (any other Django-supported DB may be used)
- psycopg2 2.7.1 - Postgres support for Django
- Whitenoise 3.3.0 - Serve static files from Django on Heroku
- dj-database-url 0.4.2 - Parse database connections from 12-factor style URLs 
- python-dotenv 0.6.4 - Parse environment variables from .env files
- django-registration-redux 1.6 -  registration app for Django
- django-crispy-forms 1.6.1- Bootstrap inspired. Best way to have Django DRY forms

NOTE:  Podium is designed to be run on Heroku but can be used on any platform
supporting [12 Factor Apps](https://12factor.net/).

## Usage ##
- Clone or download the repo.
- Use pip to install all requirements in requirements.txt
- Create a .env file from the example.env file at the root of the project.
- Edit your .env file to include your own environment values for secret keys,
database urls, etc.

- Run `python manage.py migrate` to apply all database migrations.
- Run `python manage.py createsuperuser` to create an admin user login.
- Run `python manage.py runserver --noinput` for a development environment, run
Gunicorn directly from Procfile, or use the [Django documentation](
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/) to set up a
WSGI-compliant webserver of your choice.

** Table errors in browser @admin/talks or @admin/sessions**
- Run `python manage.py makemigrations` to re-create database migrations.

## Contributing ##
[Submit an issue](https://github.com/pyatl/podium-django/issues) or see our
 [Contributing Guidelines](CONTRIBUTING.md) for pull requests.
