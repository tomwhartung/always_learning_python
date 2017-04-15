# 23-som_postgresql_exp

Repo for trying out using PostGres to store the results of the SeeOurMinds.com quiz.

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
CREATE USER seeourminds WITH PASSWORD 'abc123';            ## CREATE ROLE
CREATE DATABASE django_test owner seeourminds;             ## CREATE DATABASE
ALTER ROLE seeourminds SET client_encoding TO 'utf8';      ## ALTER ROLE
ALTER ROLE seeourminds SET default_transaction_isolation TO 'read committed';
ALTER ROLE seeourminds SET timezone TO 'UTC';              ## ALTER ROLE
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
        'NAME': 'django_test',
        'USER': 'seeourminds',
        'PASSWORD': 'abc123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

### Step (3) Make migrations:

As tomh:

```
golpy
cd 22-som_postgres_exp/Site
python3 manage.py makemigrations
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

As tomh (in the `Site/content` directory):

```
cat content/migrations/0001_initial.py:
```

The migrations create the Quiz and Score tables with only id columns - ok for now.

### Step (5) Run the migrations:

As tomh (in the `Site/content` directory):

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

As tomh (in the `Site/content` directory):

```
python3 manage.py createsuperuser   # seeourminds/seeourmind$
```

Output:

```
Superuser created successfully.
```

So far, so good.

### Step (7) Log in via browser

Access the following url:

* http://127.0.0.1:8000/admin

And login using the above username and password.

### Notes:

* We may need to update the ALLOWED_HOSTS setting in settings.py , but I am pretty sure it is ok.
* The output from running the server alerts us to the fact that there are migrations that need to be run.
* We will want to keep the sensitive values we use on the production site in environment variables.
* If there are issues, try using the 'django.db.backends.postgresql' ENGINE (instead of 'django.db.backends.postgresql_psycopg2') .

## References

TBD.

## Goals

1. Find the best way to use Postgres to store quiz results on the site

## Notes

Try and make it so we can just drop the final versions of the files we change back into the seeourminds.com site code.

* content/???????.py

## Observations

I believe working with Postgres is going to be very similar to working with MySql.

## Requirements

TBD.

