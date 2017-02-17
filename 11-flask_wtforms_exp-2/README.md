
# 11-flask_wtforms_exp-2

Get something working here that we can use on groja.com to save email addresses.

This is a second try.

## References:

Using only one (2-part) reference this time.

* https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822
* https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982

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

Run the env.sh script to enter the environment in

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 11-flask_wtforms_exp-2/Site
. env.sh
```

## Installation

Re-using virtual envirnoment created for 10-flask_wtforms_exp-1 , so there should be nothing to install.

## Starting the app

Lazy typists use the run script.

```
run.sh          # run the app (app.py)
```

