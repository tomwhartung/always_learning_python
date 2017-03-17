# 20-som_quiz_form

Repo for figuring out how to use django forms to implement the SeeOurMinds.com quiz.

## Installation

Started with current version of code from ../19-django_forms_exp .

## References

Form class: see ../19-django_forms_exp/README.md

RadioSelect class:

- https://docs.djangoproject.com/en/1.10/topics/forms/

## Goal

Use the questionnaire json to create a form allowing the user to fill out the questionnaire.

* for now, just display the form
* the plan is to use javascript to score it only in the browser - for now
* that is the next step - don't worry about it yet!

The idea is that this repo will contain only the best of the best code and we will ultimately use it on the real site.

Any experimental code that we may want to reference later should be copied to
the ../19-django_forms_exp project for possible future reference.

## Notes

We should be able to just drop these files into the seeourminds.com site code:

* content/forms.py
* content/views.py
* content/templates/content/quiz.html

We **may** need to merge this file into the seeourminds.com site code:

* content/urls.py

**See the goals and note that we do NOT want to process the quiz on the server at this time.**

## Work flow

The flow is:

1. Create or update a forms class in forms.py
2. Add a route for the form to urls.py
3a. Add code to initialize the incomplete ("unbound") form (if necessary) in views.py
3b. Add code to process the completed ("bound") form in views.py
4. Create or update the template as necessary

### forms.py

Leave only the quiz form in forms.py .

### urls.py

Unsure whether we really need to add a route, considering that for now we just want to use javascript to score the quiz in the browser.

### views.py



### Template: quiz.html

Pick and choose the code we like from ../19-django_forms_exp and use it here, adding code from the references as appropriate.

