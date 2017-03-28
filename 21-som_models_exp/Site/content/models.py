""" Contains the models for our app.

Purpose: just because we aren't using a db doesn't mean we can't have models
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none, yet)
"""

import json
import os
from django.db import models

class Quiz(models.Model):

    """ Model all the questions in the entire quiz """

    def __init__(self):
        print('Hi from the __init__() method in the Quiz!')
        self.quiz_dictionary = []

    def read_quiz_json(self):

        """ Read the quiz questions and answers from the json file """

        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        quiz_file_name = 'seeourminds_quiz.json'
        quiz_file_dir = site_content_dir + '/static/content/json/quiz/'
        quiz_file_path = quiz_file_dir + quiz_file_name
        quiz_json_file = open(quiz_file_path)
        quiz_json_string = quiz_json_file.read()
        quiz_json_file.close()
        self.quiz_dictionary = json.loads(quiz_json_string)
        return(self.quiz_dictionary)

    def get_label(self, question_no, quiz_question):

        """ Get and return the question_text ("label") for the question """

        print('get_label - question_no:', question_no)
        print('get_label - quiz_question:', quiz_question)
        label = str(question_no) + '. ' + quiz_question['question_text']
        return label

    def get_choices(quiz_question):

        """ Get and return the answers from the json for the given question """

        # print('get_choices - quiz_question:', quiz_question)
        choices = []

        if len(quiz_question['answer_1_text']) > 0 and \
           int(quiz_question['answer_1_weight']) > 0:
            choice_1 = ['1', quiz_question['answer_1_text']]
            choices.append(choice_1)

        if len(quiz_question['answer_2_text']) > 0 and \
           int(quiz_question['answer_2_weight']) > 0:
            choice_2 = ['2', quiz_question['answer_2_text']]
            choices.append(choice_2)

        if len(quiz_question['answer_3_text']) > 0 and \
           int(quiz_question['answer_3_weight']) > 0:
            choice_3 = ['3', quiz_question['answer_3_text']]
            choices.append(choice_3)

        if len(quiz_question['answer_4_text']) > 0 and \
           int(quiz_question['answer_4_weight']) > 0:
            choice_4 = ['4', quiz_question['answer_4_text']]
            choices.append(choice_4)

        if len(quiz_question['answer_5_text']) > 0 and \
           int(quiz_question['answer_5_weight']) > 0:
            choice_5 = ['5', quiz_question['answer_5_text']]
            choices.append(choice_5)

        if len(quiz_question['answer_6_text']) > 0 and \
           int(quiz_question['answer_6_weight']) > 0:
            choice_6 = ['6', quiz_question['answer_6_text']]
            choices.append(choice_6)

        return choices
