""" Placeholder models module is currently empty.

Purpose: placeholder for if and when we want to implement one or more models
Author: (none)
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.db import models

class Quiz(models.Model):

    """ Model all the questions in the entire quiz """

    def __init__():
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
