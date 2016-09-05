
## always_learning_python

Playground for my python projects.

### Installation

In case we want to do this on other hosts, here are the steps I am using, and why.

#### References

https://en.wikipedia.org/wiki/Django_(web_framework)

https://docs.djangoproject.com/en/1.10/topics/install/#                              ## 1.10 is the current version

https://docs.djangoproject.com/en/1.10/topics/install/#install-apache-and-mod-wsgi   ## skipping this and the db steps

Apparently it is included in all versions of Ubuntu but I am having difficulty finding
what version is included.  Using pip with the virtual tools seems like the best first
step because I want to try it out before installing all those packages globally.
Plus we know for sure what version we will be getting; plus see this page:

https://docs.djangoproject.com/en/1.10/topics/install/#install-the-django-code       ## Installing an official release with pip

Which points to this (seemingly unlikely) page:

https://docs.djangoproject.com/en/1.10/intro/contributing/

https://docs.djangoproject.com/en/1.10/intro/contributing/#getting-a-copy-of-django-s-development-version

Which as a side effect of describing how to set up a django patch dev area also
describes how to use virtualenv, and includes an Ubuntu-specific section

I.e. NOT running this command

```
* python3 -m venv ~/.virtualenvs/djangodev
```

Also found on install the main installation page, under "Install Django," as "Install the latest development version"

https://docs.djangoproject.com/en/1.10/topics/install/#installing-development-version


INSTEAD:

* Skip down to "For Ubuntu users" section and run the commands below.

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

> Anything you install through pip from now on will be installed in your new virtualenv, isolated from other environments and system-wide packages. Also, the name of the currently activated virtualenv is displayed on the command line to help you keep track of which one you are using. Go ahead and install the previously cloned copy of Django:

```
. ~/.virtualenvs/djangodev/bin/activate
cd /var/www/learn/django/github/customizations/always_learning_python/
git clone git://github.com/django/django.git
pip install -e django/

```


