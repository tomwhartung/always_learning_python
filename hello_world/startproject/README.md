
# hello_world - startproject versions

This is the README.md file for the hello_world/startproject directory.

* For information about getting hello_world to work with django, but in a more minimal way, etc. see ../README.md .

* For information about installing django and setting up the required virtual environments, etc. see ../../README.md .

## Why so many versions?

Right about the time I get it working, I figure out how I should have set it up.

> "It's complicated"

By running this multiple times, I am homing in how I want to set this up on the live server.

I see no problem with leaving old versions lying around, as long as there is documentation describing them.

## References

It seems wise to consult more than one source for this information; I found two that actually work, after a few tries!

* http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php
* http://dfpp.readthedocs.io/en/latest/chapter_01.html

Not using these, because it's not a "hello world" app, but checking them out as I go, and want to for possible future reference:

* https://docs.djangoproject.com/en/1.10/intro/tutorial01/    ## covers the current stable version
* https://docs.djangoproject.com/en/dev/intro/tutorial01/     ## covers the current development version

This azure tutorial is minimal (which is nice) and offers an interesting perspective, but I am not using it per se.

* https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-python-django-web-app/

Couldn't get this one to work, at least not quickly.

* https://github.com/django-ve/helloworld

Want to save for possible future reference as well.

## NOTE!

**The djangoproject tutorial says to NOT put this code in a subdirectory of /var/www .**

Interestingly, the azure tutorial says to put it in /var/www specifically (not even a subdir!).

## Guide to the Projects

* say_hi-hybrid - the first time through I

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
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/hello_world/startproject/say_hi
cd hello_dfpp
rm admin.py models.py
rm -r migrations
cd ..
```

The instructions say to edit the following files (creating them as necessary)

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/hello_world/startproject/say_hi
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

* http://localhost:8000/
* http://127.0.0.1:8000/

This is working as of 2016-09-08.

#### hello_bogo app setup

Note that we are using "**hello_bogo**" instead of "HelloWorldApp" so we must **change all the edits we make accordingly.**

Note the app name (**hello_bogo**) and use of the `django-admin` (instead of the `python`) command.

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
django-admin startapp hello_bogo          ## or: python manage.py startapp hello_bogo

```

The instructions say to edit the following files (creating them as necessary)

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/hello_world/startproject/say_hi
vi hello_bogo/views.py       ## Note: app dir
vi hello_bogo/urls.py        ## Note: app dir
vi say_hi/urls-bogo.py       ## Note: project dir - and MUST rename to settings.py when running app
vi say_hi/settings-bogo.py   ## Note: project dir - and MUST rename to settings.py when running app
```

#### Running the hello_bogo app

Start the server and browse to the app in browser:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd hello_world/startproject/say_hi
cd say_hi                         ## [sic]
cp urls-bogo.py urls.py           ## HACK - should have made separate projects
cp settings-bogo.py settings.py   ## HACK - should have made separate projects
cd ..
python manage.py runserver
```

Access in browser:

* http://localhost:8000/hello_bogo/
* http://127.0.0.1:8000/hello_bogo/

This is working as of 2016-09-08.

