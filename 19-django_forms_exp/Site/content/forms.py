##
#  forms.py: experimenting with forms to figure out the best way to
#     populate the quiz page and implement the questionnaire
#
from django import forms

##
#  NameForm: about as simple as you can get.
#  Reference:
#     https://docs.djangoproject.com/en/1.10/topics/forms/
#
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

##
#  ContactForm: the next step
#  Reference:
#     https://docs.djangoproject.com/en/1.10/topics/forms/
#
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
