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

## Notes

There are two base classes for creating forms:

- Form - just the form
- ModelForm - for storing the data in the database

### Using the Form class

We are focusing on a form for the questionnaire.
The questions and answers are already in json, and at this time, I do not forsee wanting to change them very much.

Also, for now anyway, we will **score the quiz in the browser.**

In the future, we may want to store questionnaire results and scores in the database, but this is not desired in the near term.

