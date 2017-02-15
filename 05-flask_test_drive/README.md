
# 5-flask_test_drive project

Experimenting with flask, taking it out for a test drive, so to speak.

## Two READMEs

For the process we used to get jane going, see README-jane.md in this directory.

For the process we used to get bette going, see README-bette.md in this directory.
(We may skip a step, delete some meanderings about the process, etc. in this version.)

## Reference:

Going through some examples in Chapter 2 of the "Flask Web Development" book.

Reference: http://shop.oreilly.com/product/0636920031116.do

## Goal:

Determine whether switching groja.com to flask would enable us to keep the navigation,
and other elements common to all pages, DRY.

#### DRY?

DRY = Don't Repeat Yourself.

Currently groja.com is nice and simple, but any changes to the navigation
(or many other aspects of a page, such as link tags, favicon, title, etc. -
but it is the nav that is most likely to change) need to be copy-and-pasted into all pages.

I'm thinking that the templating that flask provides should make it easy to overcome this problem.

Let's try it out, and find out for sure!

