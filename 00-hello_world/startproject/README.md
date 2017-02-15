
# hello_world - startproject versions

This is the README.md file for the 0-hello_world/startproject directory.

* For information about getting hello_world to work with django, but in a more minimal way, etc. see ../README.md .

* For information about installing django and setting up the required virtual environments, etc. see ../../README.md .

## Why so many versions?

Right about the time I got two of these actually working, I figured out how I should have set it up.

> "It's complicated"

By running this multiple times, I am homing in how I want to set this up on the live server.

I see no problem with leaving old versions lying around, as long as there is documentation describing them.

## Guide to the versions

The first time through I tried doing all of the ones listed above in one project area, what is now say_hi_hybrid.

* say_hi_hybrid - contains my first efforts

As it turned out, only two of the tutorials really had what I was looking for, so once I "finished" I went through those again, individually and much more quickly.

* say_hi_dfpp - from the same site as the ../../pure_python.py version
* say_hi_bogo - from a site run by a PhD. who seems to know about every programming language ever invented

These two were fairly consistent, but due to naming issues cannot run in the same project environment.

Plus I do not care for some of the names used (e.g., "foo") in the first place, which leads us to:

* say_hi_tomh - contains a synthesis of what I like about the other versions

## References

It seems wise to consult more than one source for this information; I found two that actually work, after a few tries!

* http://dfpp.readthedocs.io/en/latest/chapter_01.html
* http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php

Not using these, because it's not a "hello world" app, but checking them out as I go, and want to for possible future reference:

* https://docs.djangoproject.com/en/1.10/intro/tutorial01/    ## covers the current stable version
* https://docs.djangoproject.com/en/dev/intro/tutorial01/     ## covers the current development version

This azure tutorial is minimal (which is nice) and offers an interesting perspective, but I am not using it per se.

* https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-python-django-web-app/

Couldn't get this one to work, at least not quickly.

* https://github.com/django-ve/helloworld

Want to save it anyway, for possible future reference.

## NOTE!

**The djangoproject tutorial says to NOT put this code in a subdirectory of /var/www .**

Interestingly, the azure tutorial says to put it in /var/www specifically (not even a subdir!).

## say_hi_dfpp

After getting two hello_world projects running, this was done starting from scratch, mostly following this process:

* http://dfpp.readthedocs.io/en/latest/chapter_01.html

If any of this is confusing, skip to the section about the say_hi_hybrid version, which contains many more details.

### Commands Run - startproject

I used the following commands to set up this project:

```
cd /var/www/learn/django/github/customizations/always_learning_python
. ~/.virtualenvs/djangostable/bin/activate
python -m django --version    ## 1.10.2a1
cd 0-hello_world/startproject
django-admin startproject say_hi_dfpp
cd say_hi_dfpp
python manage.py runserver    ## Ctrl-C to exit
```

Ignore the migrate warnings, visit http://localhost:8000 or http://127.0.0.1:8000, and you should see django's "It worked!" screen

### Running startapp and git commit

Generate a default "**hello_dfpp_app**" app using the **python** command, and commit all generated code:

```
## pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_dfpp
## virtualenv = djangostable
python manage.py startapp hello_dfpp_app
git add .
git commit -m 'Initial commit of all generated (default) code for say_hi_dfpp and hello_dfpp_app.'
```

### Removing and editing the files

The tutorial says to delete these files, because they are not needed:

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_dfpp
cd hello_dfpp_app
rm admin.py models.py
rm -r migrations
cd ..
git commit -m 'Deleted a few files from directory hello_dfpp_app, as called for in the tutorial.'
```

The tutorial says to edit the following files, creating them as necessary:

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_dfpp
vi hello_dfpp_app/urls.py      ## Notes: new file in app dir
vi hello_dfpp_app/views.py     ## Note: app dir
vi say_hi_dfpp/settings.py     ## Note: project dir
vi say_hi_dfpp/urls.py         ## Note: project dir
```

To see what was changed, diff the original and latest versions.

### Running the app and committing the code

Start the server:

```
## pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_dfpp
## virtualenv = djangostable
python manage.py runserver
```

Access one or both of these urls in the browser:

* http://127.0.0.1:8000/
* http://localhost:8000/

If it works, commit the code:

```
git add --all .
git commit -m 'Updated app and project files in directories hello_dfpp_app and say_hi_dfpp, as called for in the tutorial.'
```

## say_hi_bogo

After getting two hello_world projects running, this was done starting from scratch, mostly following this process:

* http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php

If any of this is confusing, skip to the section about the say_hi_hybrid version, which contains many more details.

### Commands Run - startproject

I used the following commands to set up this project:

```
cd /var/www/learn/django/github/customizations/always_learning_python
. ~/.virtualenvs/djangostable/bin/activate
python -m django --version    ## 1.10.2a1
cd 0-hello_world/startproject
django-admin startproject say_hi_bogo
cd say_hi_bogo
python manage.py runserver    ## Ctrl-C to exit
```

Ignore the migrate warnings, visit http://localhost:8000 or http://127.0.0.1:8000, and you should see django's "It worked!" screen

### Running startapp and git commit

Generate a default "**hello_bogo_app**" app using the **django-admin** command (he does it a little differently), and commit the code.

```
## pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_bogo
## virtualenv = djangostable
django-admin startapp hello_bogo_app
git add .
git commit -m 'Initial commit of all generated (default) code for say_hi_bogo and hello_bogo_app.'
```

### Editing the files

The instructions say to edit the following files (creating them as necessary)

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_bogo
## vi hello_bogo_app/urls.py    ## Note: NOT NEEDED for the bogo version
vi hello_bogo_app/views.py      ## Note: app dir
vi say_hi_bogo/urls.py          ## Note: project dir
vi say_hi_bogo/settings.py      ## Note: project dir
```

To see what was changed, diff the original and latest versions.

### Running the app and committing the code

Start the server:

```
## pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_bogo
## virtualenv = djangostable
python manage.py runserver
```

Access one or both of these urls in the browser:

* http://127.0.0.1:8000/hello_bogo_app/     ## NOTE: must include the app name for the bogo version!
* http://localhost:8000/hello_bogo_app/     ## NOTE: must include the app name for the bogo version!

If it works, commit the code:

```
git add --all .
git commit -m 'Updated app and project files in directories hello_dfpp_app and say_hi_dfpp, as called for in the tutorial.'
```

## say_hi_tomh

After getting two hello_world projects running, this was done starting from scratch, mostly following this process:

* http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php

If any of this is confusing, skip to the section about the say_hi_hybrid version, which contains many more details.

### Commands Run - startproject

I used the following commands to set up this project:

```
cd /var/www/learn/django/github/customizations/always_learning_python
. ~/.virtualenvs/djangostable/bin/activate
python -m django --version    ## 1.10.2a1
cd 0-hello_world/startproject
django-admin startproject say_hi_tomh
cd say_hi_tomh
python manage.py runserver    ## Ctrl-C to exit
```

Ignore the migrate warnings, visit http://localhost:8000 or http://127.0.0.1:8000, and you should see django's "It worked!" screen

### Running startapp and git commit

I decided to use the **python** command for this, because it's what the tutorial on djangoproject.com does.

Generate a default "**hello_tomh_app**" app using the **python** command, and commit the generated code.

```
## pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_tomh
## virtualenv = djangostable
python manage.py startapp hello_tomh_app
git add .
git commit -m 'Initial commit of all generated (default) code for say_hi_tomh and hello_tomh_app.'
```

### Editing the files

Looking at output of the other two (now four) working versions, I decided to make slightly different edits in this step.

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_tomh
vi hello_tomh_app/urls.py      ## Notes: new file in app dir
vi hello_tomh_app/views.py     ## Note: app dir
vi say_hi_tomh/settings.py     ## Note: project dir
vi say_hi_tomh/urls.py         ## Note: project dir
git add .
git commit -m 'Updated app and project files in directories hello_tomh_app and say_hi_tomh, as appropriate for my own needs.'
```

To see what was changed, diff the original and latest versions.

### Running the app and committing the code

Start the server:

```
## pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_tomh
## virtualenv = djangostable
python manage.py runserver
```

Access one or both of these urls in the browser:

* http://127.0.0.1:8000/
* http://localhost:8000/

If it works, commit the code:

```
git add --all .
git commit -m 'Updated app and project files in directories hello_tomh_app and say_hi_tomh, as I am wont to do.'
```

## say_hi_hybrid

This contains my first efforts.

These instructions are baby steps and to actually run the apps you need to copy files.

I recommend looking at one of the other projects; the `hello_tomh_app` one is the last and best.

### Running the apps

These won't run "out of the box," but it's pretty easy to get them running.

First off, we need to get into the correct directory and environment:

```
cd /var/www/learn/
cd django/github/customizations/always_learning_python
. ~/.virtualenvs/djangostable/bin/activate
python -m django --version                  ## 1.10.2a1
cd startproject
cd say_hi_hybrid
```

#### Running hello_dfpp in say_hi_hybrid

To run the hello_dfpp app, *ensure you are in the djangostable environment* and enter the following commands:

```
python -m django --version  ## Should display 1.10.2a1
cd say_hi
cp settings-dfpp.py settings.py
cp urls-dfpp.py urls.py
l
cd ..
python manage.py runserver   ## Ctrl-C to stop
```

And access one or both of these URLs:

* http://localhost:8000/
* http://127.0.0.1:8000/

Cleanup: run the following commands to return the source tree to its original state:

```
cd say_hi
cp urls-save.py urls.py
cp settings-save.py settings.py
cd ..
```

#### Running hello_bogo in say_hi_hybrid

To run the hello_bogo app, *ensure you are in the djangostable environment* and enter the following commands:

```
python -m django --version  ## Should display 1.10.2a1
cd say_hi
cp settings-bogo.py settings.py
cp urls-bogo.py urls.py
l
cd ..
python manage.py runserver   ## Ctrl-C to stop
```

And access one or both of these URLs:

* http://localhost:8000/hello_bogo/
* http://127.0.0.1:8000/hello_bogo/

Cleanup: run the following commands to return the source tree to its original state:

```
cd say_hi
cp urls-save.py urls.py
cp settings-save.py settings.py
cd ..
```

### Commands Run - Setup

It seems wise to make a note of these commands, in case I like what they do and want to do it again.

```
goln                                                              ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python            ## I.e. parent dir of this repo
. ~/.virtualenvs/djangostable/bin/activate
python -m django --version                  ## 1.10.2a1
mkdir startproject
cd startproject
django-admin startproject say_hi
mv say_hi say_hi_hybrid           ## actually renamed much later but ....
cd say_hi_hybrid
```

### Files created:

These file names are relative to /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_hybrid

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

### Commands - Running the Server

Let's see if this works!

```
goln                                                              ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python            ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd startproject/say_hi_hybrid
python manage.py runserver
```

#### NOTE!

As the tutorial advises, I am ignoring warnings about unapplied migrations

> You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
> Run 'python manage.py migrate' to apply them.

### Access in Browser:

Getting "It worked!" message

* http://127.0.0.1:8000/
* http://localhost:8000/

### Creating the "hello_app" app

Here the "main" tutorial at djangoproject starts in on the polls app ("startapp polls").

Meanwhile a couple of the others show how to run "startapp" and get a hello world app.

I want to stick with "hello world," and maybe come back to the polls app in the "main" tutorial.

### Two Paths

These two tutorials use different methods to accomplish the "hello world" goal.

**1. "dfpp" - http://dfpp.readthedocs.io/en/latest/chapter_01.html**

**2. "bogo" - http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php**

I want to follow both - in parallel - then maybe I will know enough to be able to fix the version from the book.

#### Default 1: hello_dfpp_default

First generate a default "**hello_dfpp_default**" app using the **python** command:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd 0-hello_world/startproject/say_hi_hybrid
python manage.py startapp hello_dfpp_default
```

#### Default 2: hello_bogo_default

Now generate a default "**hello_bogo_default**" app using the **django-admin** command:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd 0-hello_world/startproject/say_hi_hybrid
django-admin startapp hello_bogo_default
```

Keeping this generated code as-is, for easy reference as we follow the tutorials and change code in the other apps.

#### Diffing the defaults

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

### hello_dfpp app setup

Note the app name (*hello_dfpp*) and use of the python (instead of the django-admin) command.

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd 0-hello_world/startproject/say_hi_hybrid
python manage.py startapp hello_dfpp      ## or: django-admin startapp hello_dfpp
```

#### Removing and editing the files

The instructions say to delete these files, because they are not needed:

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_hybrid
cd hello_dfpp
rm admin.py models.py
rm -r migrations
cd ..
```

The instructions say to edit the following files (creating them as necessary)

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_hybrid
vi hello_dfpp/urls.py        ## Note: app dir
vi hello_dfpp/views.py       ## Note: app dir
vi say_hi/settings-dfpp.py   ## Note: project dir - and MUST rename to settings.py when running app
vi say_hi/urls-dfpp.py       ## Note: project dir - and MUST rename to urls.py when running app
```

To see what was changed, diff the original and latest versions.

### Running the hello_dfpp app

Start the server and browse to the app in the browser:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd 0-hello_world/startproject/say_hi_hybrid
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

### hello_bogo app setup

Note that we are using "**hello_bogo**" instead of "HelloWorldApp" so we must **change all the edits we make accordingly.**

Note the app name (**hello_bogo**) and use of the `django-admin` (instead of the `python`) command.

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd 0-hello_world/startproject/say_hi_hybrid
django-admin startapp hello_bogo          ## or: python manage.py startapp hello_bogo

```

#### Editing the files

The instructions say to edit the following files (creating them as necessary)

```
## In pwd = /var/www/learn/django/github/customizations/always_learning_python/0-hello_world/startproject/say_hi_hybrid
## vi hello_bogo/urls.py     ## Note: NOT NEEDED for bogo version
vi hello_bogo/views.py       ## Note: app dir
vi say_hi/urls-bogo.py       ## Note: project dir - and MUST rename to settings.py when running app
vi say_hi/settings-bogo.py   ## Note: project dir - and MUST rename to settings.py when running app
```

To see what was changed, diff the original and latest versions.

### Running the hello_bogo app

Start the server and browse to the app in browser:

```
goln                                                     ## cd /var/www/learn/ ** *BAD but OK for now* **
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
. enter_djangostable_env.sh
cd 0-hello_world/startproject/say_hi_hybrid
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

