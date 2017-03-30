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


class Score(models.Model):

    """ Class to contain the score for the quiz """

    def __init__(self):
        self.e_score = 0
        self.i_score = 0
        self.n_score = 0
        self.s_score = 0
        self.f_score = 0
        self.t_score = 0
        self.j_score = 0
        self.p_score = 0

    def tally_answer(self, answer_123_type, answer_selected, answer_weight):
        print('Score.tally_answer - answer_123_type:', answer_123_type)
        print('Score.tally_answer - answer_selected:', answer_selected)
        print('Score.tally_answer - answer_weight:', answer_weight)


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

    def get_quiz_question(self, list_question_no):

        """ Return the entire quiz question (answers, weights, etc.)"""

        quiz_question = self.question_list[list_question_no]
        # print('Quiz.get_quiz_question - list_question_no:', list_question_no)
        # print('Quiz.get_quiz_question - quiz_question:', quiz_question)
        return quiz_question

    def get_label(self, list_question_no):

        """ Get and return the question_text ("label") for the question """
        """ list_question_no is 0 based, the question ids and labels are 1-based """

        quiz_question = self.get_quiz_question(list_question_no)
        form_question_no = list_question_no + 1
        label = str(form_question_no) + '. ' + quiz_question['question_text']
        # print('Quiz.get_label - list_question_no:', list_question_no)
        # print('Quiz.get_label - label:', label)
        return label

    def get_choices(self, list_question_no):

        """ Return the answer choices for the given question """

        quiz_question = self.get_quiz_question(list_question_no)
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

        # print('Quiz.get_choices - list_question_no:', list_question_no)
        # print('Quiz.get_choices - len(choices):', len(choices))
        return choices

    def get_answer_123_type(self, list_question_no):

        """ Get and return the answer_123_type (e.g., "E") for the question """

        quiz_question = self.get_quiz_question(list_question_no)
        answer_123_type = quiz_question['answer_123_type']
        return answer_123_type

    def get_answer_text(self, list_question_no, answer_selected):

        """ Get and return the answer_X_text for the selected answer 'X' """

        quiz_question = self.get_quiz_question(list_question_no)
        answer_text_key = "answer_" + answer_selected + "_text"
        answer_text = quiz_question[answer_text_key]
        return answer_text

    def get_answer_weight(self, list_question_no, answer_selected):

        """ Get and return the answer_X_weight for the selected answer 'X' """

        quiz_question = self.get_quiz_question(list_question_no)
        answer_weight_key = "answer_" + answer_selected + "_weight"
        answer_weight = quiz_question[answer_weight_key]
        return answer_weight

    def score_quiz(self, cleaned_data):

        """ Process the data from the form and set the scores """
        """ question_list is 0 based, the form questions are 1-based """

        print('Quiz.score_quiz - cleaned_data:', cleaned_data)
        score = Score()

        for form_question_str in sorted(cleaned_data):
            form_question_no = int(form_question_str.replace("question_", ""))
            list_question_no = int(form_question_no) - 1
            answer_123_type = self.get_answer_123_type(list_question_no)
            answer_selected = cleaned_data[form_question_str]
            answer_text = self.get_answer_text(list_question_no, answer_selected)
            answer_weight = self.get_answer_weight(list_question_no, answer_selected)

            # print('form_question_str:',  str(form_question_str))
            print('form_question_no:',  str(form_question_no))
            # print('list_question_no:',  str(list_question_no))
            print('answer_123_type:',  answer_123_type)
            print('answer_selected:',  answer_selected)
            print('answer_text:',  answer_text)
            print('answer_weight:',  answer_weight)

            score.tally_answer(answer_123_type, answer_selected, answer_weight)










