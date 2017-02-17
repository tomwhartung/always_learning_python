
# flask_wtforms_exp-1

Get something working here that we can use on groja.com to save email addresses.

This is a first try.

I think that by amalgamating too many sources, I kind of confused myself.

## References:

I think that by amalgamating too many sources, I kind of confused myself.

### Starting references

Combining ideas from Chapters 3 & 4 of the "Flask Web Development" book.

Reference: http://shop.oreilly.com/product/0636920031116.do

Using the db design from ../08-real_python_class/2017_02_07-Lesson_2/class_projects/calculator .

### Additional references

When the first attempt didn't work very well, I went searching for additional information, and added some ideas found in these:

* https://www.tutorialspoint.com/flask/flask_wtf.htm
* http://flask.pocoo.org/docs/0.12/patterns/wtforms/

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
cd 10-flask_wtforms_exp-1/Site
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
