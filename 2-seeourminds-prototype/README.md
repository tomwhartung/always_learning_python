
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

This is where we start merging in the html5boilerplate initializr stuff.

##### Removed one level of directories

When I started on this section, the files were in:

* `2-seeourminds-prototype/Site/seeourminds/*`

where the `*` includes a directory named seeourminds.

So I removed the seeourminds directory at the first level; "hope that's OK."



