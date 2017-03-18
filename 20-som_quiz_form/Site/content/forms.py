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
   choices_12 = get_choices( quiz_dictionary[11] )
   question_12 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_12 )
   choices_13 = get_choices( quiz_dictionary[12] )
   question_13 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_13 )
   choices_14 = get_choices( quiz_dictionary[13] )
   question_14 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_14 )
   choices_15 = get_choices( quiz_dictionary[14] )
   question_15 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_15 )
   choices_16 = get_choices( quiz_dictionary[15] )
   question_16 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_16 )
   choices_17 = get_choices( quiz_dictionary[16] )
   question_17 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_17 )
   choices_18 = get_choices( quiz_dictionary[17] )
   question_18 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_18 )
   choices_19 = get_choices( quiz_dictionary[18] )
   question_19 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_19 )
   choices_20 = get_choices( quiz_dictionary[19] )
   question_20 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_20 )

   choices_21 = get_choices( quiz_dictionary[20] )
   question_21 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_21 )
   choices_22 = get_choices( quiz_dictionary[21] )
   question_22 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_22 )
   choices_23 = get_choices( quiz_dictionary[22] )
   question_23 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_23 )
   choices_24 = get_choices( quiz_dictionary[23] )
   question_24 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_24 )
   choices_25 = get_choices( quiz_dictionary[24] )
   question_25 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_25 )
   choices_26 = get_choices( quiz_dictionary[25] )
   question_26 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_26 )
   choices_27 = get_choices( quiz_dictionary[26] )
   question_27 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_27 )
   choices_28 = get_choices( quiz_dictionary[27] )
   question_28 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_28 )
   choices_29 = get_choices( quiz_dictionary[28] )
   question_29 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_29 )
   choices_30 = get_choices( quiz_dictionary[29] )
   question_30 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_30 )

   choices_31 = get_choices( quiz_dictionary[30] )
   question_31 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_31 )
   choices_32 = get_choices( quiz_dictionary[31] )
   question_32 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_32 )
   choices_33 = get_choices( quiz_dictionary[32] )
   question_33 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_33 )
   choices_34 = get_choices( quiz_dictionary[33] )
   question_34 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_34 )
   choices_35 = get_choices( quiz_dictionary[34] )
   question_35 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_35 )
   choices_36 = get_choices( quiz_dictionary[35] )
   question_36 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_36 )
   choices_37 = get_choices( quiz_dictionary[36] )
   question_37 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_37 )
   choices_38 = get_choices( quiz_dictionary[37] )
   question_38 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_38 )
   choices_39 = get_choices( quiz_dictionary[38] )
   question_39 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_39 )
   choices_40 = get_choices( quiz_dictionary[39] )
   question_40 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_40 )

   choices_41 = get_choices( quiz_dictionary[40] )
   question_41 = forms.ChoiceField( widget=forms.RadioSelect, choices=choices_41 )




