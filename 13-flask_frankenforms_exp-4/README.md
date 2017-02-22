
# 13-flask_frankenforms_exp-4

Get something working here that we can use on groja.com to save email addresses.

This is the fourth and hopefully last try, where we combine everything we've learned and try to get to something usable.

## References:

See:

* ../10-flask_wtforms_exp-1
* ../11-flask_wtforms_exp-2
* ../12-flask_wtforms_exp-3

## Goals:

Create a simple form to save email addresses in an SqlLite database.

### Goal: Assimilate previous experiments and get something usable

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
cd 13-flask_frankenforms_exp-4/Site
. env.sh
```

## Installation

Need to install flask-wtf and flask-bootstrap.

```
pip install flask
pip install flask-wtf
```

## Starting the app

Lazy typists use the run script.

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 13-flask_frankenforms_exp-4/Site
run.sh          # run the app (app.py)
```

