
# always_learning_python

Playground for my python projects.

## Installation: References, Process, Etc.

In case we want to do this on other hosts, here are the steps I am using, and why.

### References

General references, to get us started:

* https://en.wikipedia.org/wiki/Django_(web_framework)
* https://docs.djangoproject.com/en/1.10/topics/install/#                              ## 1.10 is the current version
* https://docs.djangoproject.com/en/1.10/topics/install/#install-apache-and-mod-wsgi   ## skipping this and the db steps

Apparently it is included in all versions of Ubuntu but I am having difficulty finding
what version is included.  Using pip with the virtual tools seems like the best first
step because I want to try it out before installing all those packages globally.
Plus we know for sure what version we will be getting; plus see this page:

* https://docs.djangoproject.com/en/1.10/topics/install/#install-the-django-code       ## Installing an official release with pip

Which points to this (seemingly unlikely) page:

* https://docs.djangoproject.com/en/1.10/intro/contributing/
* https://docs.djangoproject.com/en/1.10/intro/contributing/#getting-a-copy-of-django-s-development-version

Which as a side effect of describing how to set up a django patch dev area also
describes how to use virtualenv, and includes an Ubuntu-specific section

I.e. NOT running this command

```
* python3 -m venv ~/.virtualenvs/djangodev
```

Also found on install the main installation page, under "Install Django," as "Install the latest development version"

* https://docs.djangoproject.com/en/1.10/topics/install/#installing-development-version

INSTEAD:

* Skip down to "For Ubuntu users" section and run the commands under "Installation" below.

About virtualenv:

* https://virtualenv.pypa.io/en/stable/
* https://virtualenvwrapper.readthedocs.io/en/latest/

### Installation:

```
  sudo apt-get install python3-pip
  pip3 install virtualenv
  sudo apt install virtualenv   ## Also had to do this for some strange reason...
  virtualenv --python=`which python3` ~/.virtualenvs/djangodev
```

### Activation:

```
. ~/.virtualenvs/djangodev/bin/activate
```

### Use:

> "Anything you install through pip from now on will be installed in your new virtualenv, isolated from other environments and system-wide packages. Also, the name of the currently activated virtualenv is displayed on the command line to help you keep track of which one you are using. Go ahead and install the previously cloned copy of Django:"

```
. ~/.virtualenvs/djangodev/bin/activate
cd /var/www/learn/django/github/customizations/always_learning_python/
git clone git://github.com/django/django.git
sudo pip install -e django/
```

### Verify:

Before entering virtual environment:

```
which python   ## /usr/bin/python
python -V      ## Python 2.7.12
python         ## skipping output before prompt
>>> import django
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named django
>>>
```

After entering virtual environment:

```
. ~/.virtualenvs/djangodev/bin/activate
which python                 ## /home/tomh/.virtualenvs/djangodev/bin/python
python -V                    ## Python 3.5.2
python -m django --version   ## 1.11.dev20160903160000
python                       ## skipping output before prompt
>>> import django
>>> print(django.get_version())
1.11.dev20160903160000
>>> django.__path__
['/var/www/learn/django/github/customizations/always_learning_python/django/django']
>>>
```

### Setting up the djangostable Environment:

Create new virtual environment that runs the current stable version of django (on branch stable/1.10x).

* https://github.com/django/django/tree/stable/1.10.x

#### Create the environment

```
goln                                                              ## cd /var/www/learn/
cd django/github/customizations/always_learning_python            ## I.e. parent dir of this repo
virtualenv --python=`which python3` ~/.virtualenvs/djangostable
cp virtualenvs/enter_djangodev_env.sh virtualenvs/enter_djangostable_env.sh
vi virtualenvs/enter_djangostable_env.sh
ga virtualenvs/enter_djangostable_env.sh
gc 'Adding virtualenvs/enter_djangostable_env.sh .'
gpom
. virtualenvs/enter_djangostable_env.sh      ## enter the new djangostable environment
```

#### Clone and checkout stable version of django

```
goln                      ## cd /var/www/learn/
cd django/github/django
mkdir djangostable
cd djangostable
git clone git@github.com:django/django.git
cd django
git checkout stable/1.10.x
```

#### Enter the environment and install stable version of django

```
goln                                                     ## cd /var/www/learn/
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. virtualenvs/enter_djangostable_env.sh                  ## enter the new djangostable environment
goln                      ## cd /var/www/learn/
cd django/github/django/djangostable
pip install django
```

#### Verify

```
python -V                    ## Python 3.5.2
python -m django --version   ##  1.10.2a1
python                       ## (output appearing before prompt omitted)
>>> import django
>>> print(django.get_version())
1.10.2a1
>>> django.__path__
['/home/tomh/.virtualenvs/djangostable/lib/python3.5/site-packages/django']
>>> exit()
```

Good job!

## hello_world Project

1. Lightweight Django Book version - does not work - yet (wip)
2. pure_python.py version - works in new virtual environment (see below)
3. startproject version - created using startproject: there are a few of these onlin (see below)

### 1. Lightweight Django Book version

See lightweight_django_book.py .

Unable to get this to work, yet (after entering the command, it simply returns).

**WIP (Work in Progress)**

Notes:
* I found several other versions of hello world that use startproject (trying one or more of those next)
* The book is using version 1.8 of django, we are using 1.10 (maybe set up a virtual env using 1.8 and try that?)

### 2. pure_python.py version

#### References:

* http://dfpp.readthedocs.io/en/latest/chapter_01.html   ## where I got the code
* https://pypi.python.org/pypi/six/#downloads            ## where I got the six library
* http://python-future.org/compatible_idioms.html        ## differences between python 2 and 3

#### Setting up the "six" virtual environment

We do not want to always have six installed by default in our environment, so we set up a new one for it:

```
virtualenv --python=`which python` ~/.virtualenvs/six    ## creates the environment
```

Note: I tried specifying "--python=`which python3`" but that kept giving me "Network Unreachable" errors (??).

```
. ~/.virtualenvs/six/bin/activate    ## enter the environment (command saved in enter_six_env.sh for easy reference)
python
>>> import six                       ## gives an error because it is not yet installed in this environment
>>> exit()
goln                                                     ## cd /var/www/learn/
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
mkdir unpack
cp downloads/six-1.10.0.tar.gz unpack
cd unpack
tar -xvzf six-1.10.0.tar.gz
rm six-1.10.0.tar.gz
pip install six-1.10.0
python
>>> import six        ## No error means the setup was successful
>>> exit()
```
#### Running the pure_python.py version

Enter the following commands to start the server and serve the greetings:

```
. ~/.virtualenvs/six/bin/activate                        ## enter the environment (see enter_six_env.sh)
goln                                                     ## cd /var/www/learn/
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
python hello_world/pure_python.py                        ## Access localhost:8000 in browser for "hello" greetins

```

### 3. startproject version

See hello_world/startproject directory.

#### References

It seems wise to consult more than one source for this information.

* https://docs.djangoproject.com/en/1.10/intro/tutorial01/                  ## looks like the best one
* http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php
* http://dfpp.readthedocs.io/en/latest/chapter_01.html
* https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-python-django-web-app/

Not using this one but checking it out as I go, so it's worth saving for possible future reference:

* https://docs.djangoproject.com/en/dev/intro/tutorial01/   ## covers the current development version

Couldn't get this one to work, at least not quickly; saving for possible future reference as well:

* https://github.com/django-ve/helloworld

##### NOTE!

**The djangoproject tutorial says to NOT put this code in a subdirectory of /var/www .**

Interestingly, the azure tutorial says to put it in /var/www specifically (not even a subdir!).

#### Commands Run - Setup

It seems wise to make a note of these commands, in case I like what they do and want to do it again.

```
goln                                                              ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python            ## I.e. parent dir of this repo
. ~/.virtualenvs/djangostable/bin/activate
python -m django --version                  ## 1.10.2a1
mkdir using_startproject
cd startproject
django-admin startproject say_hi
cd say_hi
```

#### Files created:

These file names are relative to /var/www/learn/django/github/customizations/always_learning_python/hello_world/startproject/say_hi

* `manage.py` - for site administration; similar to using ```django-admin``` or ```python -m django``` (see link below)
* `say_hi` - the python package name for this project; use when importing code, e.g., say_hi/urls
* `say_hi/__init__.py` - empty file that tells Python that this directory should be considered a Python package
* `say_hi/settings.py` - application and database settings; for details, see link below
* `say_hi/urls.py` - the "table of contents" for your site; for details, see link below
* `say_hi/wsgi.py` - Web Server Gateway Interface; an entry point that enables handling requests and serving pages via apache

Links:

* https://docs.djangoproject.com/en/1.10/ref/django-admin/   ## for using manage.py, django-admin, etc.
* https://docs.djangoproject.com/en/1.10/topics/settings/    ## django settings reference
* https://docs.djangoproject.com/en/1.10/topics/http/urls/   ## url dispatcher reference

#### Commands - Running the Server

Let's see if this works!

```
goln                                                              ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python            ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd startproject/say_hi
python manage.py runserver
```

##### NOTE!

As the tutorial advises, I am ignoring warnings about unapplied migrations

> You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
> Run 'python manage.py migrate' to apply them.

#### Access in Browser:

Getting "It worked!" message

* http://127.0.0.1:8000/
* http://localhost:8000/

#### Creating the "hello_app" app

Here the "main" tutorial at djangoproject starts in on the polls app ("startapp polls").

Meanwhile a couple of the others show how to run "startapp" and get a hello world app.

I want to stick with "hello world," and maybe come back to the polls app in the "main" tutorial.

#### Two Paths

These two tutorials use different methods to accomplish the "hello world" goal.

**1. "dfpp" - http://dfpp.readthedocs.io/en/latest/chapter_01.html**

**2. "bogo" - http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php**

I want to follow both - in parallel - then maybe I will know enough to be able to fix the version from the book.

##### Default 1: hello_dfpp_default

First generate a default "**hello_dfpp_default**" app using the **python** command:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
python manage.py startapp hello_dfpp_default
```

##### Default 2: hello_bogo_default

Now generate a default "**hello_bogo_default**" app using the **django-admin** command:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
django-admin startapp hello_bogo_default
```

Keeping this generated code as-is, for easy reference as we follow the tutorials and change code in the other apps.

##### Diffing the defaults

Note that the class name in apps.py is different for all four generated trees.

Other than that, the hello_bogo_default (django-admin) version contains the following lines not found in the hello_dfpp_default (python tartapp) version:

```
< # -*- coding: utf-8 -*-
< from __future__ import unicode_literals
```

in the following files:

* `admin.py`
* `apps.py`
* `models.py`
* `tests.py` and
* `views.py`

Not huge differences, but I want to ensure we have the cleanest diff output possible, while still closely following the tutorials.

#### hello_dfpp app setup

Note the app name (*hello_dfpp*) and use of the python (instead of the django-admin) command.

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
python manage.py startapp hello_dfpp      ## or: django-admin startapp hello_dfpp
```

The instructions say to delete these files, because they are not needed:

```
## In cwd = /var/www/learn/django/github/customizations/always_learning_python/hello_world/startproject/say_hi
cd hello_dfpp
rm admin.py models.py
rm -r migrations
cd ..
```

The instructions say to edit the following files (creating them as necessary)

```
## In cwd = /var/www/learn/django/github/customizations/always_learning_python/hello_world/startproject/say_hi
vi hello_dfpp/urls.py        ## Note: app dir
vi hello_dfpp/views.py       ## Note: app dir
vi say_hi/settings-dfpp.py   ## Note: project dir - and MUST rename to settings.py when running app
vi say_hi/urls-dfpp.py       ## Note: project dir - and MUST rename to urls.py when running app
```

#### Running the hello_dfpp app

Start the server and browse to the app in the browser:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
cd say_hi                            ## [sic]
cp settings-dfpp.py settings.py      ## HACK - should have made separate projects
cp urls-dfpp.py urls.py              ## HACK - should have made separate projects
cd ..
python manage.py runserver
```

Access in browser:

* http://localhost:8000
* http://127.0.0.1:8000/

This is working as of 2016-09-08.

#### hello_bogo app setup

Note that we are using "hello_bogo" instead of "HelloWorldApp" so we must **change all the edits we make accordingly.**

Note the app name (*hello_bogo*) and use of the django-admin (instead of the python) command.

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
django-admin startapp hello_bogo          ## or: python manage.py startapp hello_bogo

```

The instructions say to edit the following files (creating them as necessary)

```
## In cwd = /var/www/learn/django/github/customizations/always_learning_python/hello_world/startproject/say_hi
vi hello_bogo/views.py       ## app dir
vi hello_bogo/urls.py        ## app dir
vi say_hi/urls.py            ## project dir
vi say_hi/settings-bogo.py   ## project dir - rename to settings.py when running app
```

#### Running the hello_bogo app

Start the server and browse to the app in browser:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
cd say_hi                            ## [sic]
cp settings-bogo.py settings.py      ## HACK!!!
cd ..
python manage.py runserver
```

Access in browser:

* http://localhost:8000/hello_bogo

(Aaaaaaaaand, rats - it doesn't work.)






