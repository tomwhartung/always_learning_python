
# 14-flask_frankenform_with_db

Get something working here that we can use on groja.com to save email addresses.

This is the most recent version of the form, which we like ok, with code to save the entered values in a sqlite database.

## References:

See:

* ../10-flask_wtforms_exp-1
* ../11-flask_wtforms_exp-2
* ../12-flask_wtforms_exp-3
* ../13-flask_frankenforms_exp-4

## Goals:

Create a simple form to save email addresses in an SqlLite database.

### Goal: Use the form to save rows in the db

We may want to use this for gathering emails for more than one site.

Using schema from the not-quite-finished django version in ../04-polls_to_emails .

* name - TEXT
* email - TEXT
* site - TEXT
* active - INTEGER
* date_added - INTEGER
* date_changed - INTEGER
* consulting - INTEGER
* newsletter - INTEGER
* portrait - INTEGER

## Environment

Run the env.sh script to enter the environment in

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 14-flask_frankenform_with_db/Site
. env.sh
```

## Installation

The virtual environment we are using has flask-wtf and flask-bootstrap already installed.
Sqlite3 is already included in python3.

```
pip install flask       # needed only if using this code in a new project
pip install flask-wtf   # needed only if using this code in a new project
```

## Creating the db and table

Running `db.py`:

1. if the db is pressent, drops the db and table
2. creates the db and table
3. inserts a sample row into the table

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 14-flask_frankenform_with_db/Site
. env.sh
python -m db_create
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
cd 14-flask_frankenform_with_db/Site
run.sh          # run the app (app.py)
```

