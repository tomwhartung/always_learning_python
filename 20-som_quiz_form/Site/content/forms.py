##
#  forms.py: forms used by the app
#     1. populate the quiz page and implement the questionnaire
#     2. ???
#
from django import forms

##
#  QuizForm: the next step
#  Reference:
#     https://docs.djangoproject.com/en/1.10/topics/forms/
#
class QuizForm(forms.Form):
    name = forms.CharField( max_length=50 )
    email = forms.EmailField()
