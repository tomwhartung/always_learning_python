
# 6-flask_templates_exp project

More experiments with flask.

Note that these experiments build on what we did in ../5-flask_test_drive .

## Reference:

Continuing with playing around with examples from the "Flask Web Development" book, this time from Chapter 3.

Reference: http://shop.oreilly.com/product/0636920031116.do

## Goal:

Determine whether switching groja.com to flask would enable us to keep the navigation,
and other elements common to all pages, DRY.

These options seem to work ok, and the -h option makes it the site available from other hosts - good to know!

## Flask Bootstrap

Experiment with the following goal in mind:

* Decide whether we want to use flask bootstrap, or just include a link tag as we do in the current version of groja.com .

**Try both options, examine the source, and decide.**

## Flask and Handlebars

I am confident that the templates can help keep groja.com's navigation, footer, etc. more DRY.

However, Jinga2's templating syntax resembles that of handlebars, so I wonder whether I can combine them.
I actually think I can, by sending the handlebars code to the template in a variable,
rather than including handlebars code in the template itself.

* Determine whether we can use flask with handlebars.

**Focus on trying to replicate one of the gallery pages in an experiment.**

