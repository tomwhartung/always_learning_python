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

      if len(quiz_question['answer_2_text']) > 0 and int(quiz_question['answer_2_weight']) > 0 :
         choice_2 = [ '2', quiz_question['answer_2_text'] ]
         choices.append( choice_2 )

      if len(quiz_question['answer_3_text']) > 0 and int(quiz_question['answer_3_weight']) > 0 :
         choice_3 = [ '3', quiz_question['answer_3_text'] ]
         choices.append( choice_3 )

      if len(quiz_question['answer_4_text']) > 0 and int(quiz_question['answer_4_weight']) > 0 :
         choice_4 = [ '4', quiz_question['answer_4_text'] ]
         choices.append( choice_4 )

      if len(quiz_question['answer_5_text']) > 0 and int(quiz_question['answer_5_weight']) > 0 :
         choice_5 = [ '5', quiz_question['answer_5_text'] ]
         choices.append( choice_5 )

      if len(quiz_question['answer_6_text']) > 0 and int(quiz_question['answer_6_weight']) > 0 :
         choice_6 = [ '6', quiz_question['answer_6_text'] ]
         choices.append( choice_6 )

      return choices

   name = forms.CharField( max_length=50 )
   email = forms.EmailField()
   quiz_dictionary = read_quiz_json()
   ## print( 'quiz_dictionary:', quiz_dictionary )
   print( 'len(quiz_dictionary):', len(quiz_dictionary) )
   ## print( 'quiz_dictionary[0]:', quiz_dictionary[0] )

   choices_01 = get_choices( quiz_dictionary[0] )
   question_01 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_01 )
   choices_02 = get_choices( quiz_dictionary[1] )
   question_02 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_02 )
   choices_03 = get_choices( quiz_dictionary[2] )
   question_03 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_03 )
   choices_04 = get_choices( quiz_dictionary[3] )
   question_04 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_04 )
   choices_05 = get_choices( quiz_dictionary[4] )
   question_05 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_05 )
   choices_06 = get_choices( quiz_dictionary[5] )
   question_06 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_06 )
   choices_07 = get_choices( quiz_dictionary[6] )
   question_07 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_07 )
   choices_08 = get_choices( quiz_dictionary[7] )
   question_08 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_08 )
   choices_09 = get_choices( quiz_dictionary[8] )
   question_09 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_09 )
   choices_10 = get_choices( quiz_dictionary[9] )
   question_10 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_10 )
   choices_11 = get_choices( quiz_dictionary[10] )
   question_11 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_11 )

