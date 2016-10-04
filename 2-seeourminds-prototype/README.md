
# 2-seeourminds-prototype

Experimenting with a possible replacement for seeourminds.com .

### The Goal

The goal of this project is to merge

* what we learned in the hello-world django project with
* the html5boilerplate initializr-responsive (no optionals) template

### The initializr-responsive-* directories

Downloaded these from http://www.initializr.com/ , using the middle option "Responsive"

* initializr-responsive-1-no_optionals - checked no checkboxes under "H5BP Optional"

* initializr-responsive-2-defaults - checked only defaults under "H5BP Optional"

* initializr-responsive-3-all_optionals_checked - checked all checkboxes under "H5BP Optional"

If merging the bare minimum (under 1-no_optionals) works OK, try adding in files from the 2-defaults and 3-all_optionals_checked directories as desired.

### Site directory

#### Start the project

Ran these commands to start the project:

```
cd 2-seeourminds-prototype/
mkdir Site
cd Site
. ~/.virtualenvs/djangostable/bin/activate
python -m django --version
django-admin startproject seeourminds
cd seeourminds/
python manage.py runserver      ## site is accessible on the localhost only
ga .
gc 'Results from running startproject, checked in the browser (works on localhost only).'
```

#### Start the app

Ran these commands to start the app:

```
django-admin startapp home
ga home/
gc 'Adding the default, generated version of files created running "django-admin startapp home" .'
```

#### Editing the files

There are two steps:

1. Get the django 0-hello_world minimal app going

2. Merge in the html5boilerplate initializr stuff

#### Removed one level of directories

When I started on this section, the files were in:

* `2-seeourminds-prototype/Site/seeourminds/*`

where the `*` includes a directory named seeourminds.

So I removed the seeourminds directory at the first level; "hope that's OK."

### Hello world meets seeourminds

Looking back at ../0-hello_world/startproject , it appears that say_hi_tomh combines the best parts of the various versions there.

* `home/views.py` - added `class HomePageView` etc.
* `home/urls.py`  - added urlpattern for the home page and replaced call to pattern function with a simple array definition
* `seeourminds/urls.py` - removed all generated code and added url pattern directing blank urls to the routes in home.urls
* `seeourminds/settings.py` - added app definition and commented out database stuff

The comments in all edits reference the dfpp tutorial, so you can follow along using this reference:

* http://dfpp.readthedocs.io/en/latest/chapter_01.html#writing-the-code

#### Running the server

Use these commands to run the server:

```
. ~/.virtualenvs/djangostable/bin/activate
python manage.py runserver
```

And access the site in the browser:

* http://127.0.0.1:8000/

#### Check in to git

```
git add ...
git commit ...
```

### Django meets html5boilerplate

Start by adding in markup from

* `initializr-responsive-1-no_optionals/index.html`

into

* `Site/home/views.py`

Hey it works - sorta....

### Html5boilerplate meets Django

It looks like we can get this to work, but first, it's back to the main tutorial, to learn about templates and static files.

References:

* https://docs.djangoproject.com/en/1.10/intro/tutorial03/ - views
* https://docs.djangoproject.com/en/1.10/intro/tutorial06/ - static files (css & js)

Baby steps:

1. Added index function to views.py
2. Updated both urls.py files
3. We are moving away from the say_hi_tomh/dfpp way of doing things towards following the djangoproject.com tutorial more closely
4. Commiting current changes and carrying on with the djangoproject.com tutorial ...

### Getting the template to work

Moving on to part 3 of the tutorial, skipping the polls-specific stuff to get to the "Write views that actually..." section

* https://docs.djangoproject.com/en/1.10/intro/tutorial03/#write-views-that-actually-do-something

More baby steps:

1. Created file `home/templates/home/index.html` with some markup such that we will know it if we are seeing it
2. Added import command to views.py: `from django.template import loader`
3. Updated the index() function in views.py to call the loader on the template and render it with a null context (1)
4. Commit the baby step changes!

(1) That may sound complicated but seriously, just look at the index() function in views.py, it is like three lines of code.

**Return to learn the render shortcut and how to do 404 pages**

* https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-render
* https://docs.djangoproject.com/en/1.10/intro/tutorial03/#raising-a-404-error

### Moving html5boilerplate code to the index template

We have the index file where we want it, that just leaves the css and js; Django calls these "static" files.

References:

* https://docs.djangoproject.com/en/1.10/intro/tutorial06/ - how-to for css files
* https://docs.djangoproject.com/en/1.10/howto/static-files/ - other types: images, etc.

1. Replaced `home/templates/home/index.html` with the html5boilerplate index.html
2. Added a context variable to both it and home/views.py to test that functionality (it works as expected)
3. Commit the baby step changes!
4. Move the css files into the new directory `home/static/home/css`
5. Update the index.html (template) file with `{% load static %}` and adjust the link tags for the css files
6. Commit the baby step changes!

