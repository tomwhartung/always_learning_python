
# 5-flask_test_drive project

Experimenting with flask, taking it out for a test drive, so to speak.

## Setting up jane:

This is the process we used to set up flask on jane.
It may contain some steps and meanderings not essential to the task.

For the process used to set up flask on bette, which may be a bit more focused and less wordy, see README-bette.md in this directory.

## Step (0) Optional: Clone source used in book

Did this on barbara and jane.
Wound up not using it on barbara, so you could say we did it on jane "just for grins."

Following the book, grabbing a copy of his code, and using virtualenv.

```
cd /var/www/learn/django/github
mkdir miguelgrinberg
cd miguelgrinberg
git clone git@github.com:miguelgrinberg/flasky.git
cd flasky/
git checkout 1a
virtualenv venv
```

The last command creates a venv subdirectory in `/var/www/learn/django/github/miguelgrinberg/flasky/` .

If it is not already there, create a tiny shell script to allow easy access to the virtual env.

```
cd /var/www/learn/django/github/customizations/always_learning_python/
cd virtualenvs/
cat > enter_venv.sh
cat enter_venv.sh
. /var/www/learn/django/github/miguelgrinberg/flasky/venv/bin/activate
```

Run the shell script, and use pip3 and **sudo -H ** to install flask:

```
. ./enter_venv.sh
which pip3                 ## /usr/bin/pip3
sudo -H pip3 install flask
```

Check:

```
python3
>>> import flask        ## No error message -> success!
>>> flask.__version__   ## '0.11.1'
>>>
deactivate         ## exits the virtual environment
```

Use the venv virtual environment when experimenting with the code from the book.
So far we have been "doing our own thing," so now we will create our own virtual environment and use that.

### Note:

**Running these steps installs flask 0.11.1 globally as well!**

## Step (1) Install Flask Globally

As discovered by running the steps above, creating a virtualenv and installing flask in it makes it available globally anyway.

**We can worry about using virtual environments when it comes time to upgrade.**

```
sudo -H pip3 install flask
```

Check:

```
python3
>>> import flask        ## No error message -> success!
>>> flask.__version__   ## '0.11.1'
>>>
deactivate         ## exits the virtual environment
```

Fwiw, it is also present in the virtual environment (even though we uninstalled it from there!).

## Step (2) Basics

Create a hello world app, and play with it a bit.

```
cd always_learning_python/5-flask_test_drive/
mkdir Site
cd Site
vi hello.py
```

#### Basic Hello World

Update hello.py with code from the book, then run the app:

```
cd always_learning_python/5-flask_test_drive/
cd Site/
python3 hello.py
```

Access in browser:

* http://127.0.0.1:5000/
* http://localhost:5000/

#### Going Beyond Hello World

Add new route and function to hello.py, personalizing its message, and access it in browser again to test.

```
vi hello.py
```

Update the index function to get and display the user agent string.

## Step (3) Flask-Script

Copy hello.py to script.py, add in flask script, and play with it a bit.

```
cp hello.py script.py
vi script.py
```

```
sudo -H pip3 install flask-script
```

See text near the end of chapter 2.

Interesting - got this warning:

```
/usr/local/lib/python3.5/dist-packages/flask/exthook.py:71: ExtDeprecationWarning: Importing flask.ext.script is deprecated, use flask_script instead.
```

Easy enough to fix.

Need to run it like this:

```
python3 script.py --help         ## not very much help
python3 script.py runserver -?   ## that's more like it
python3 script.py runserver
python3 script.py runserver -h 10.0.0.113
python3 script.py runserver -h 10.0.0.113 -p 6001
```

These options seem to work ok, and the -h option makes it the site available from other hosts - good to know!

## Conclusion - NOT

We have not yet accomplished the goal we set out to accomplish, but I want to leave this directory as-is for now.

## To Be Continued

For more experiments and their results, see directory ../6-flask_templates_exp .
