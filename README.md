
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

## hello_world Project

I found multiple versions of the hello_world project, and played around with them quite a bit, so it has its own README.md files.

