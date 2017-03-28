# 21-som_models_exp

Repo for figuring out whether we want to use the django models class in working with the SeeOurMinds.com quiz.

## Installation

Started with current version of code from groja.com/Site

## References

TBD.

## Goals

1. Create a model class

2. Move the json file handling code from the forms class to the new models class

3. Find the best way to do this on the site

## Notes

We should be able to just drop the final versions of the files we change back into the seeourminds.com site code:

* content/forms.py
* content/models.py
* content/???????.py

## Observations

* The django models class seems to be designed for working with databases.

* We are working with json.

Hence, we are just experimenting.

## Requirements

The model needs to be able to:

* populate itself by loading the json

* Allow access to questions, answers, weights, etc.

