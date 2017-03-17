##
#  forms.py: forms used by the app
#     1. populate the quiz page and implement the questionnaire
#     2. ???
#
from django import forms

##
#  QuizForm: convert our json to a list of questions and multiple-choice answers
#
class QuizForm(forms.Form):
   def get_choices( question_no ):
      choices = [[ '1', 'First choice'], ['2', 'Second choice']]

   name = forms.CharField( max_length=50 )
   email = forms.EmailField()
   ## choices_1 = get_choices(1)
   ## choices_1 = ( ( '1', 'First choice', ), ('2', 'Second choice', ) )
   choices_1 = [[ '1', 'First choice'], ['2', 'Second choice']]
   question_1 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_1 )
