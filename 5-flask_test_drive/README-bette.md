
# 5-flask_test_drive project

Experimenting with flask, taking it out for a test drive, so to speak.

## Setting Up bette

We are starting the process from scratch, on bette.

For the process we used to get jane going, see README-jane.md in this directory.
(We may skip a step, delete some meanderings about the process, etc. in this version.)

## Reference:

Going through some examples in Chapter 2 of the "Flask Web Development" book.

Reference: http://shop.oreilly.com/product/0636920031116.do

## Goal:

Determine whether switching groja.com to flask would enable us to keep the navigation,
and other elements common to all pages, DRY.

## Step (1): Install virtualenv, pip3, and flask

For consistency with the other hosts, install virtualenv.
We wound up not using it on barbara or jane, so you could say we are doing it "just for grins."
However, I am sure it will come in handy in the future.

```
dpkg-query --list '*virtualenv*'
sudo apt-get install virtualenv
```

That should install pip3, if it doesn't install it like so:

```
sudo apt-get -y install python3-pip
sudo apt-get -s install python-pip
```

I see no reason to install pip for python2, but if it's needed it can be installed by changing the -s (for simulate) to -y.

```
cd /var/www/learn/github/customizations/always_learning_python/
cd virtualenvs/
virtualenv flask_bette
cat > flask_bette_env.sh
cat flask_bette_env.sh
. /var/www/always_learning/github/customizations/always_learning_python/virtualenvs/flask_bette/bin/activate
```

Run the shell script, and use pip3 and **sudo -H ** to install flask:

```
. ./flask_bette_env.sh
which pip3                 ## /usr/bin/pip3
sudo -H pip3 install flask
```

Check:

```
python3
>>> import flask        ## No error message -> success!
>>> flask.__version__   ## '0.12'
>>>
deactivate         ## exits the virtual environment
```

We should use the venv virtual environment when experimenting with the code from the book.
However, I can find pip3 (did not try running it) and import flask outside of the environment.

**We can worry about using virtual environments when it comes time to upgrade.**

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
python3 script.py runserver -h 10.0.0.112          # http://10.0.0.112:6001/
python3 script.py runserver -h 10.0.0.112 -p 6001  # http://10.0.0.112:6001/
```

These options seem to work ok, and the -h option makes it the site available from other hosts - good to know!

## Conclusion - NOT

We have not yet accomplished the goal we set out to accomplish, but I want to leave this directory as-is for now.

## To Be Continued

For more experiments and their results, see directory ../6-flask_templates_exp .
