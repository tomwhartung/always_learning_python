
# 10-flask_save_emails_exp

Get something working here that we can use on groja.com to save email addresses.

## References:

Combining ideas from Chapters 3 & 4 of the "Flask Web Development" book.

Reference: http://shop.oreilly.com/product/0636920031116.do

Using some db code from ../08-real_python_class/2017_02_07-Lesson_2/class_projects/calculator .

## Goal:

Create a simple form to save email addresses in an SqlLite database.

## Schema

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
cd 10-flask_save_emails_exp/Site
. env.sh
```

## Installation

Need to install flask-wtf and flask-bootstrap.
Sqlite3 is already included in python3.

```
pip3 install flask-wtf
pip3 install flask-bootstrap
```

## Starting the app

Lazy typists use the run script.

```
hello-run.sh    # sanity check
run.sh          # run the app (app.py)
```
