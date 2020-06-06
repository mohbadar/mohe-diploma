#### Reset Migrations

```
1-

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete


Drop the current database, or delete the db.sqlite3 if it is your case.

python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations


for app:

python manage.py migrate --fake core zero
python manage.py showmigrations


```


#### Postgres DB

```

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo su - postgres

CREATE DATABASE eformdb;

CREATE USER eform_user WITH PASSWORD 'secret';

ALTER ROLE eform_user SET client_encoding TO 'utf8';
ALTER ROLE eform_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE eform_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE eformdb TO eform_user;

pip install django psycopg2

settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eformdb',
        'USER': 'eform_user',
        'PASSWORD': 'secret',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000 

