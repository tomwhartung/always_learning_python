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
class QuizForm( forms.Form ):
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

   ##
   #  Get and return the answers that are populated in the json for the given question
   #
   def get_choices( quiz_question ):
      print( 'get_choices - quiz_question:', quiz_question )
      choices = []
      if len(quiz_question['answer_1_text']) > 0 and int(quiz_question['answer_1_weight']) > 0 :
         choice_1 = [ '1', quiz_question['answer_1_text'] ]
         choices.append( choice_1 )

      ## choices = [[ '1', 'get_choices: first choice'], ['2', 'get_choices: second choice' ]]
      return choices

   name = forms.CharField( max_length=50 )
   email = forms.EmailField()
   quiz_dictionary = read_quiz_json()
   ## print( 'quiz_dictionary:', quiz_dictionary )
   print( 'len(quiz_dictionary):', len(quiz_dictionary) )
   print( 'quiz_dictionary[0]:', quiz_dictionary[0] )
   ## choices_1 = [[ '1', 'First hard-coded choice'], ['2', 'Second hard-coded choice']]
   choices_1 = get_choices( quiz_dictionary[0] )
   question_1 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_1 )
