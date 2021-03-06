# 23-som_postgresql_exp

Repo for trying out using PostGres to store the results of the SeeOurMinds.com quiz.

## References

Installation:

* https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04
* https://tutorial.djangogirls.org/en/django_start_project/
* https://tutorial.djangogirls.org/en/django_admin/

Models, postgresql:

* TBD.

## Goal

1. Find the best way to use Postgres to store quiz results on the site

2. Try and make it so we can just drop the final versions of the files we change back into the seeourminds.com site code.

* ../../gitignored/Site/Site/settings.py
* Site/bin/*.sh           # not all have changed but many added, so grab 'em all
* Site/urls.py
* content/admin.py
* content/database.py     # NEW!
* content/forms.py
* content/models.py
* content/urls.py
* content/views.py
* content/static/content/css/seeourminds.css
* content/templates/content/base.html
* content/templates/content/quiz.html
* content/templates/content/quiz_results.html

## Installation

Started with current version of code from seeourminds.com/Site .

### Step (0) Install Postgres in Ubuntu, and use it to create a user and a database.

See instructions in the following file in the jmws_accoutrements repo:

* doc/ubuntu/specific_hosts/2016-bette/5-updating_python_etc.txt

#### Summary of commands run (copied from 5-updating_python_etc.txt):

As root:

```
apt-get install libpq-dev postgresql postgresql-contrib
su - postgres
psql        # prompt changes
```

Use the postgres shell to create the user and database:

```
CREATE USER som_user WITH PASSWORD 'abc123';            ## "CREATE ROLE"
CREATE DATABASE som_db owner som_user;             ## "CREATE DATABASE"
ALTER ROLE som_user SET client_encoding TO 'utf8';      ## "ALTER ROLE"
ALTER ROLE som_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE som_user SET timezone TO 'MST';              ## "ALTER ROLE"
\q      ## log out

### Step (1) Install python postgres "psycopg2" package globally:

As root:

```
pip3 install psycopg2
```

### Step (2) Update settings:

Add the following code to settings.py:

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'som_db',
        'USER': 'som_user',
        'PASSWORD': 'abc123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

### Step (3) Make migrations:

As tomh:

```
golpy
cd 23-som_postgresql_exp/Site/bin
./makemigrations.sh
```

The output from this command is below.
Note that this picked up the models for my score and quiz.

```
Migrations for 'content':
  content/migrations/0001_initial.py:
    - Create model Quiz
    - Create model Score
```

### Step (4) Review migrations:

As tomh (in the `Site/` directory):

```
cat content/migrations/0001_initial.py:
```

The migrations create the Quiz and Score tables with only id columns - ok for now.

### Step (5) Run the migrations:

As tomh (in the `Site/` directory):

```
python3 manage.py migrate
```

The output from this command is below.
Looks like all of the migrations ran ok.

```
Operations to perform:
  Apply all migrations: admin, auth, content, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying content.0001_initial... OK
  Applying sessions.0001_initial... OK
```

### Step (6) Enable the admin interface:

As tomh (in the `Site/` directory):

```
(1) python3 manage.py createsuperuser
(2) python3 manage.py changepassword tomh   # tomh/djangofresh1
```

Output:

```
(1) Superuser created successfully.
(2) Password changed successfully for user 'tomh'
```

### Step (7) Run the server

As tomh (in the `Site/` directory):

```
python3 manage.py runserver
```

Access the following url:

* http://127.0.0.1:8000/

### Step (8) Log in via browser

Access the following url:

* http://127.0.0.1:8000/admin

And login using the above username and password.

## Notes:

* We may need to update the ALLOWED_HOSTS setting in settings.py , but I am pretty sure it is ok.
* The output from running the server alerts us to the fact that there are migrations that need to be run.
* We will want to keep the sensitive values we use on the production site in environment variables.
* If there are issues, try using the 'django.db.backends.postgresql' ENGINE (instead of 'django.db.backends.postgresql_psycopg2') .


## To start from scratch with a new db

### Kill app

If it's running, exit the app.

### Drop and recreate

Drop the db and recreate it, using commands from Step (0):

As root:

```
su - postgres
psql        # prompt changes
```

Use the postgres shell to drop and re-create the database:

```
DROP DATABASE som_db;
CREATE DATABASE som_db owner som_user;
ALTER ROLE som_user SET client_encoding TO 'utf8';
ALTER ROLE som_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE som_user SET timezone TO 'MST';
\q
```
```

### Make and run the migrations

#### Delete old files

First delete the old migrations files, they are irrelevant because we are starting fresh!

As tomh:

```
golpy
cd 23-som_postgresql_exp/Site/content/migrations
rm 000*
```

#### Create new file

Make and run the migrations them, using commands from steps (3) and (5)

As tomh:

```
golpy
cd 23-som_postgresql_exp/Site/bin
./makemigrations.sh
./catmigrations.sh
./migrate.sh
```

### Create django superuser

Create the superuser, using commands from Step (6):

As tomh (in the `Site/bin/` directory):

```
createsuperuser.sh    # tomh/mark_as_spam@tomhartung.com/superuser1
```
