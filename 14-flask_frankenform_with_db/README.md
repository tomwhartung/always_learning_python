
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

* name - char, 45
* email - char, 254
* site_code - char, 2
* subscribed - boolean
* subscription_date - date

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

## Starting the app

Lazy typists use the run script.

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 14-flask_frankenform_with_db/Site
run.sh          # run the app (app.py)
```

