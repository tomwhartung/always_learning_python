##
#  forms.py: forms used by the app
#     1. populate the quiz page and implement the questionnaire
#     2. ???
#
from django import forms
import json
import os

##
#  QuizForm: convert our json to a list of questions and multiple-choice answers
#
class QuizForm(forms.Form):
   quiz_dictionary = []

   ##
   #  Read the quiz questions and answers from the json file
   #
   def read_quiz_json():
      site_content_dir = os.path.abspath(os.path.dirname(__file__))
      quiz_file_name = 'seeourminds_quiz.json'
      quiz_file_path = site_content_dir + '/static/content/json/quiz/' + quiz_file_name
      quiz_json_file = open( quiz_file_path )
      quiz_json_string = quiz_json_file.read()
      quiz_json_file.close()
      quiz_dictionary = json.loads( quiz_json_string )
      return( quiz_dictionary )

   def get_choices( question_no ):
      ## print( 'self.quiz_dictionary:', self.quiz_dictionary )
      print( 'question_no:', question_no )
      choices = [[ '1', 'get_choices: first choice'], ['2', 'get_choices: second choice' ]]
      return choices

   name = forms.CharField( max_length=50 )
   email = forms.EmailField()
   choices_1 = get_choices( 1 )
   ## choices_1 = [[ '1', 'First choice'], ['2', 'Second choice']]
   question_1 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_1 )
   quiz_dictionary = read_quiz_json()
   ## print( 'quiz_dictionary:', quiz_dictionary )
   print( 'len(quiz_dictionary):', len(quiz_dictionary) )

