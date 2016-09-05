
## always_learning_python

Playground for my python projects.

### Installation

In case we want to do this on other hosts, here are the steps I am using, and why.

#### References

https://en.wikipedia.org/wiki/Django_(web_framework)
https://docs.djangoproject.com/en/1.10/topics/install/#                              ## 1.10 is the current version
https://docs.djangoproject.com/en/1.10/topics/install/#install-apache-and-mod-wsgi   ## skipping this and the db steps
#
# Apparently it is included in all versions of Ubuntu but I am having difficulty finding
# what version is included.  Using pip with the virtual tools seems like the best first
# step because I want to try it out before installing all those packages globally.
# Plus we know for sure what version we will be getting; plus see this page:
#
https://docs.djangoproject.com/en/1.10/topics/install/#install-the-django-code       ## Installing an official release with pip
#
# Which points to this (seemingly unlikely) page:
#
https://docs.djangoproject.com/en/1.10/intro/contributing/
#
# Which as a side effect of describing how to set up a django patch dev area also
# describes how to use virtualenv, and includes an Ubuntu-specific section
# I.e. NOT running this command
#   python3 -m venv ~/.virtualenvs/djangodev
# INSTEAD: skip down to "For Ubuntu users" section.
#
https://docs.djangoproject.com/en/1.10/intro/contributing/#getting-a-copy-of-django-s-development-version
#
# Installation:
#
  sudo apt-get install python3-pip
  pip3 install virtualenv
  sudo apt install virtualenv   ## Also had to do this for some strange reason...
  virtualenv --python=`which python3` ~/.virtualenvs/djangodev
#
# Activation:
#
. ~/.virtualenvs/djangodev/bin/activate




