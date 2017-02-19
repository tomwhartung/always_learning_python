
# 12-flask_wtforms_exp-3

Get something working here that we can use on groja.com to save email addresses.

This is the third try.

## References:

Using only one reference (again) this time.

* https://pythonspot.com/flask-web-forms/

This one looks to be more up-to-date, based on the `from wtforms import ...` statement.
The others used `from flask.ext.wtforms import ...` , which is deprecated.

## Goals:

Create a simple form to save email addresses in an SqlLite database.

### Goal 1 - Follow the tutorial

There are many ways to do this, looking at too many of them can get to be confusing.
This time let's stick with just this one tutorial.

### Goal 2 - Implement This Schema

We may want to use this for gathering emails for more than one site.

Using schema from the not-quite-finished django version in ../04-polls_to_emails .

* name - char, 45
* email - char, 254
* site_code - char, 2
* subscribed - boolean
* subscription_date - date

## Environment

**NOTE: This tutorial uses python2 (the print statement in the hello() function throws an error in python3).**

Run the env.sh script to enter the environment in

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 12-flask_wtforms_exp-3/1-name/Site
. env.sh
```

## Installation

**NOTE: Use the `pip` command instead of `pip3` to install these modules because this tutorial uses python2.**

Need to install flask-wtf and flask-bootstrap.
Sqlite3 is already included in python3.

```
pip install flask
pip install flask-wtf
```

## Starting the app

Lazy typists use the run script.

### (1) Form with only the name field

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 12-flask_wtforms_exp-3/1-name/Site
run.sh          # run the app (app.py)
```

### (2) Form with only the name field and bootstrap styles

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 12-flask_wtforms_exp-3/2-name_bootstrap/Site
run.sh          # run the app (app.py)
```

### (3) Registration form

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 12-flask_wtforms_exp-3/3-registration_form/Site
run.sh          # run the app (app.py)
```

