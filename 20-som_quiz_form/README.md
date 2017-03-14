# 19-django_forms_exp

Repo for experimenting with django forms.

## Installation

Started with current version of code for seeourminds.com .

Updated settings.py by changing the secret key etc.

Installed django globally on bette:

As root:

```
pip3 install django==1.10.2
```

## References

Form class:

- https://docs.djangoproject.com/en/1.10/topics/forms/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

For now.

ModelForm class:

- https://tutorial.djangogirls.org/en/django_forms/
- https://tutorial.djangogirls.org/en/django_models/

For later.

## Goals

1. Use the questionnaire json to create a form allowing the user to fill out the questionnaire
2. Play around with django form capability to discover the best way to do this

The idea is to experiment a bit and actually port only the best of the best code into the real site,
leaving any interesting experiments here for possible future reference.

## Notes

There are two base classes for creating forms:

- Form - just the form
- ModelForm - for storing the data in the database

### Using the Form class

We are focusing on a form for the questionnaire.
The questions and answers are already in json, and at this time, I do not forsee wanting to change them very much.

Also, for now anyway, we will **score the quiz in the browser.**

In the future, we may want to store questionnaire results and scores in the database, but this is not desired in the near term.

## Work flow

The flow is:

1. Create or update a forms class in forms.py
2. Add a route for the form to urls.py
3a. Add code to initialize the incomplete ("unbound") form (if necessary) in views.py
3b. Add code to process the completed ("bound") form in views.py
4. Create or update the template as necessary

### forms.py

Put **all** experimental forms in forms.py .

### urls.py

Don't be afraid to use longish, descriptive routes.

### views.py

Feel free to add a view for each variation of each form.

We will pick and choose the code we like from here when the time comes.

### Template: quiz.html

Use quiz.html as the template for all forms.

We will pick and choose the code we like from here when the time comes.

