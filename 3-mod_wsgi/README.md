
# 3-mod_wsgi project

The Apache mod_wsgi module allows us to use Apache to serve sites written in python (and django).

This is just a test area we can use for performing and tracking this process.

### Main References:

Much of this is based on information on this page:

* https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html

When I want a second opinion, I go to this page - scroll past the first 2/3 of it and see the "Configure Apache" section:

* https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04

For references and specific steps, see doc/ubuntu/general/1-process_checklist-jane.txt in the jmws_accoutrements repo.


### The `Site` Directory

This directory contains code to test installation and configuration of mod_wsgi .

* `Site/sample_app.py` - sample application - "the WSGI application script file"

