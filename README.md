
# always_learning_python

Playground for my python projects.

## Installation: References, Process, Etc.

In case we want to do this on other hosts, here are the steps I am using, and why.

#### References

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

#### TODO:

Figure out how to use the stable version on branch stable/1.10x:

* https://github.com/django/django/tree/stable/1.10.x


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

## hello_world Project

1. Version from book did not work (book using version 1.8 of django, we are using 1.10)
2. Got pure_python.py version to work in new virtual environment (see below)
3. Django version ... (wip - see below)

### hello_world - pure_python.py version

References:

Where I got the code:

* http://dfpp.readthedocs.io/en/latest/chapter_01.html

Where I got the six library:

* https://pypi.python.org/pypi/six/#downloads

A nice page describing the differences between versions 2 and 3 of python:

* http://python-future.org/compatible_idioms.html

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

### hello_world - hello_django.py version

WIP

