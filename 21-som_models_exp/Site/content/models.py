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

site_content_dir = os.path.abspath(os.path.dirname(__file__))
QUIZ_FILE_DIR = site_content_dir + '/static/content/json/quiz/'
QUIZ_FILE_NAME = 'seeourminds_quiz.json'

class Quiz(models.Model):

    """ Model all the questions in the entire quiz """

    def __init__(self):

        """ Populate the question_list with questions from the json file """

        self.question_list = self.read_quiz_json()


    def read_quiz_json(self):

        """ Read the quiz questions and answers from the json file """

        quiz_file_path = QUIZ_FILE_DIR + QUIZ_FILE_NAME
        quiz_json_file = open(quiz_file_path)
        quiz_json_string = quiz_json_file.read()
        quiz_json_file.close()
        question_list = json.loads(quiz_json_string)
        return(question_list)


    def get_quiz_question(self, question_no):

        """ Return the entire quiz question (answers, weights, etc.)"""

        quiz_question = self.question_list[question_no]
        print('Quiz.get_quiz_question - question_no:', question_no)
        # print('Quiz.get_quiz_question - quiz_question:', quiz_question)
        return quiz_question


    def get_label(self, question_no):

        """ Get and return the question_text ("label") for the question """

        # question_no is 0 based, we want the labels to be 1-based
        quiz_question = self.get_quiz_question(question_no)
        label = str(question_no+1) + '. ' + quiz_question['question_text']
        # print('Quiz.get_label - question_no:', question_no)
        # print('Quiz.get_label - label:', label)
        return label


    def get_choices(self, question_no):

        """ Return the answer choices for the given question """

        quiz_question = self.get_quiz_question(question_no)
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

        # print('Quiz.get_choices - question_no:', question_no)
        print('Quiz.get_choices - len(choices):', len(choices))
        return choices


    def score_quiz(self, cleaned_data):

        """ Process the data from the form and set the scores """
        """ question_list is 0 based, the form questions are 1-based """

        # for question_no, form_answer in cleaned_data:
        # for question_no in cleaned_data:
        # for (question_no, form_answer) in cleaned_data:
        for question_no in cleaned_data:
            print('question_no:',  question_no)
            print('cleaned_data[question_no]:', cleaned_data[question_no])
