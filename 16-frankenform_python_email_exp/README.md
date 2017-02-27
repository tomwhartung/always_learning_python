
# 16-frankenform_python_email_exp

Get app to send an email when someone shares their name and email address.

Starting point for this project is all the files in ../14-flask_frankenform_with_db .

## References:

See:

* ../14-flask_frankenform_with_db

## Goal:

Update ../14-flask_frankenform_with_db to send an email when someone shares their email address.

## Environment

Run the env.sh script to enter the environment in virtualenvs/p3_flask_bootstrap_wtf_bette

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 15-flask_email_exp/Site
. env.sh
```

## Installation

Starting a new virtual environment.  We need flask-wtf, flask-bootstrap, and flask-mail.
Sqlite3 is already included in python3.

```
pip3 install flask==0.12    # needed for code copied from ../14-flask_frankenform_with_db
pip3 install flask-wtf      # needed for code copied from ../14-flask_frankenform_with_db
```

## Creating the db and table

Running `db_create.py`:

1. if the db is present, drops the db and table
2. creates the db and table
3. inserts a sample row into the table

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 15-flask_email_exp/Site
. env.sh
python3 -m db_create
```

## Testing the db

To test the db, e.g., after changing the schema or something else:

```
. env.sh
python
>>> from db_access import test_insert_functions
>>> test_insert_functions()
```

We are currently only using insert functionality in the programs.
To see all rows, run print.sh (see below).  Currently that's all the functionality we need!

I tried to find a way to password-protect the db, the way we do oure mysql dbs, but was unable to.

## Printing all rows in the db

To print out all rows in the db:

```
. env.sh
./print.sh             # one way
python -m db_access    # another way - but with more typing!
```

## Starting the app

Lazy typists use the run script.

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 15-flask_email_exp/Site
run.sh          # run the app (app.py)
```

