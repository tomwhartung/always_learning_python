
# 17-frankenform_no_dupl_emails

Get app to send an email when someone shares their name and email address.

Starting point for this project is all the files in ../14-flask_frankenform_with_db .

## References:

See:

* ../14-flask_frankenform_with_db

## Goal:

Update ../16-frankenform_python_email_exp to not allow duplicate email addresses (update existing record instead).

## Environment

Run the env.sh script to enter the environment in virtualenvs/p3_flask_bootstrap_wtf_bette

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 17-frankenform_no_dupl_emails
. env.sh
```

## Installation

We are re-using the virtual environment we used in ../14-flask_frankenform_with_db , so no installation is required.

## Creating the db and table

Running `db_create.py`:

1. if the db is present, drops the db and table
2. creates the db and table
3. inserts a sample row into the table

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 17-frankenform_no_dupl_emails
. env.sh
python3 -m db_create
```

## Starting the app

NOTE: app.py has been renamed to groja.py , for consistency with the site.

Use the run script to run the app (i.e., groja.py).

```
golpy  # /var/www/always_learning/github/customizations/always_learning_python/
cd 16-frankenform_python_email_exp/Site
run.sh          # run the app (app.py)
```

## Testing the db

To test the db, e.g., after changing the schema or something else:

```
. env.sh
python
>>> from db_access import test_insert_functions
>>> test_insert_functions()
```

## Printing all rows in the db

To print out all rows in the db:

```
. env.sh
./print.sh             # one way
python -m db_access    # another way - but with more typing!
```

