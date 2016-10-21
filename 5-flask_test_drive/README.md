
# 5-flask_test_drive project

Experimenting with parts of djangoproject.com's polls app, attempting to apply the steps to a simple app that stores emails.

## Reference:

Bought a few new books today - Flask, PWAs, React Native - very exciting!

Reference: http://shop.oreilly.com/product/0636920031116.do

Gasp!  Imagine that - an actual book this time!!

## Goal:

Determine whether switching groja.com to flask would enable us to keep the navigation,
and other elements common to all pages, DRY.

#### What?

DRY = Don't Repeat Yourself.

Currently groja.com is nice and simple, but any changes to the navigation
(or many other aspects of a page, such as link tags, favicon, title, etc. -
but it is the nav that is most likely to change) need to be copy-and-pasted into all pages.

I'm thinking that the templating that flask provides should make it easy to overcome this problem.

Let's try it out, and find out for sure!

## (1) Installation

Following the book, grabbing a copy of his code, and using virtualenv (it's a bit too early to commit to a version and all).

```
cd /var/www/learn/django/github
mkdir miguelgrinberg
cd miguelgrinberg
git clone git@github.com:miguelgrinberg/flasky.git
virtualenv venv
```

Create a tiny shell script to allow easy access to the virtual env, run it, and use pip3 and **sudo -H ** to install flask:

```
cd /var/www/learn/django/github
cd virtualenvs/
cat > enter_venv.sh
cat enter_venv.sh
. /var/www/learn/django/github/miguelgrinberg/flasky/venv/bin/activate
. ./enter_vev.sh
which pip3
sudo -H pip3 install flask
```

Check:

```
python3
>>> import flask   ## No error message -> success!
>>>
deactivate         ## exits the virtual environment
```

## (2) Basics

Hello world app:

```
cd always_learning_python/5-flask_test_drive/
mkdir Site
cd Site
vi hello.py
```

Run the app:

```
cd always_learning_python/virtualenvs/
. enter_venv.sh
cd ../5-flask_test_drive/
cd Site/
python3 hello.py
```

Access in browser:

* http://127.0.0.1:5000/

Add new route and function to hello.py, personalizing its message, and access it in browser again to test.

```
vi hello.py
```

Update the index function to get and display the user agent string.


