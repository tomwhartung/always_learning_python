# 22-som_postgres_exp

Repo for trying out using PostGres to store the results of the SeeOurMinds.com quiz.

## Installation

Started with current version of code from seeourminds.com/Site .

### Install Postgres in Ubuntu

See instructions in the following file in the jmws_accoutrements repo:

* doc/ubuntu/specific_hosts/2016-bette/5-updating_python_etc.txt

### Update settings:

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

### Make migrations:

As tomh:

```
golpy
cd 22-som_postgres_exp/Site
python3 manage.py makemigrations
```

The output from this command follows.
Note that this picked up the models for my score and quiz.

```
Migrations for 'content':
  content/migrations/0001_initial.py:
    - Create model Quiz
    - Create model Score
```

### Review migrations:

As tomh:

```
cat content/migrations/0001_initial.py:
```

The migrations create the Quiz and Score tables with only id columns - ok for now.


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

