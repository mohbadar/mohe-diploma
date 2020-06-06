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
python manage.py migrate --fake core zero


```