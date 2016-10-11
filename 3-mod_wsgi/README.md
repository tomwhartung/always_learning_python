
# 3-mod_wsgi project

The Apache mod_wsgi module allows us to use Apache to serve sites written in python (and django).

This is just a test area we can use for performing and tracking this process.

### Main References:

Much of this is based on information on this page:

(1) https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html

When I want a second opinion, I go to this page - scroll past the first 2/3 of it and see the "Configure Apache" section:

(2) https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04

For references and specific steps, see doc/ubuntu/general/1-process_checklist-jane.txt in the jmws_accoutrements repo.

### The `documents` Directory

Decided to create this and put a simple "Hello world" index.html file in it.

The first Main Reference (1) uses a documents directory for the DocumentRoot, and I just want to closely follow that example and get this going.

I believe this is analogous the the `static` directory used in the second Main Reference (2).

### The `Site` Directory

This directory contains code to test installation and configuration of mod_wsgi .

* `Site/sample_app.py` - sample application - "the WSGI application script file"

### Directories and Security Concerns

So we are always reading about how the python code should be outside of DocumentRoot, for security reasons.

It's bad to put it in home directories as well - but that's where our virtualenv stuff goes by default.  "Make up your mind, guys!"

* For now, since it is a minimal site and I am checking everything into github anyway, we are going to focus on just getting it working.

Famous last words but still....

