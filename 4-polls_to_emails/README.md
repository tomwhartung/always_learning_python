
# 4-polls_to_emails project

Experimenting with parts of djangoproject.com's polls app, attempting to apply the steps to a simple app that stores emails.

### Goal:

Following the steps in the tutorial for the polls app, we want to try making an app that stores emails in a database.

(1) Initially we want to gather the email addresses of people who visit a site and are interested in more information.
(2) There will not be any sort of online access to these; if and when we use them it will be from behind a firewall.
(3) If and when we do use them, we will want to provide an interface for unsubscribing from the list.

For this application, we will use SQLite.

### Main References:

Most of this is based on information on this page:

(1) https://docs.djangoproject.com/en/1.10/intro/tutorial01/

If I need a second opinion, I will probably go to the O'Reilly book, Lightweight Django:

(2) http://shop.oreilly.com/product/0636920032502.do

However, I am learning that the djangoproject site seems to really be the best source of information.

### The `documents` Directory

Decided to create this and put a simple "Hello world" index.html file in it.

This may come in handy some day - possibly for sharing static content between apps - especially if I already have it.

### The `Site` Directory

This directory contains the code we are writing, based on the polls app but modified for our simple email gathering app.

