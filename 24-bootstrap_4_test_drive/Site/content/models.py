""" Contains the models for our app.

Purpose: contains the models for data in json format and in database
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none, yet)
"""

import json
import os
from django.db import models
from django.utils import timezone

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')

"""
There are 88 questions, and the ones I have the most confidence in are
nearer the beginning, with the "fun," experimental ones at the end.
It is desireable that the quiz size be divisible by 4 but not 8,
so that there is an odd number of questions for each pair of opposites.
"""
XX_SMALL = '2XS'       # 4 = 1*4 (for testing, keep off menu in production)
EXTRA_SMALL = 'XS'     # 12 = 3 * 4
SMALL = 'S'            # 28 = 7 * 4
MEDIUM = 'M'           # 44 = 11 * 4
LARGE = 'L'            # 60 = 15 * 4
EXTRA_LARGE = 'XL'     # 76 = 19 * 4
XX_LARGE = '2XL'       # 88 = 22 * 4


class Quiz(models.Model):

    """
    Define columns and save a person's quiz answers in the database.
    """

    QUIZ_SIZE_CHOICES = (
        (XX_SMALL, '2X Small'),
        (EXTRA_SMALL, 'Extra Small'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra Large'),
        (XX_LARGE, '2X Large'),
    )
    DEFAULT_QUIZ_SIZE = MEDIUM
    DEFAULT_QUIZ_SIZE_SLUG = 'medium'
    QUIZ_VERSION = '1.0'

    name = models.CharField(
            blank=True,
            default='',
            max_length=200)
    email = models.EmailField(
            blank=False,
            db_index=True,
            max_length=200,
            unique=True)
    size = models.CharField(
            choices=QUIZ_SIZE_CHOICES,
            default=DEFAULT_QUIZ_SIZE,
            max_length=3)
    version = models.CharField(
            default=QUIZ_VERSION,
            max_length=10)
    date_created = models.DateTimeField(
            default=timezone.now)
    date_updated = models.DateTimeField(
            default=timezone.now)

    def save_quiz(self, cleaned_data, quiz_size_slug=DEFAULT_QUIZ_SIZE_SLUG):
        """
        If we have an email, save the quiz data, along with the answers
        There is no sense saving it if we do not have an email address!
        The check here may be redundant, but this is very important!
        Note also: the validation criteria for the db is stronger than
          it is for forms...!
        """
        email = cleaned_data['email']
        if len(email) < 4:    # "blank=False" does not seem to work?!?
            print('Quiz.save_quiz - not saving! email:', '"' + email + '"')
            return False
        else:
            name = cleaned_data['name']
            self.name = name
            self.email = email
            self.size = self.get_quiz_size_abbreviation_for_slug(quiz_size_slug)
            self.save()
            print('Quiz.save_quiz - saved name/email:', name + '/' + email)
            for form_question_str in sorted(cleaned_data):
                if not form_question_str.startswith("question_"):
                    continue
                question_int = int(form_question_str.replace("question_", ""))
                answer_str = cleaned_data[form_question_str]
                answer_int = int(answer_str)
                answer_db = Answer()
                answer_db.save_answer(self.id, question_int, answer_int)
        return self

    @classmethod
    def get_quiz_size_abbreviation_for_slug(cls, quiz_size_slug):
        """ Returns the corresponding constant for passed in quiz_size_slug """
        quiz_size_constant_for_slug = {
            "xx-small": XX_SMALL,
            "extra-small": EXTRA_SMALL,
            "small": SMALL,
            "medium": MEDIUM,
            "large": LARGE,
            "extra-large": EXTRA_LARGE,
            "xx-large": XX_LARGE,
        }
        return quiz_size_constant_for_slug[quiz_size_slug]

    @classmethod
    def get_question_count_for_slug(cls, quiz_size_slug):
        """ Returns the number of questions for passed in quiz_size_slug """
        question_count_for_slug = {
            "xx-small": 4,
            "extra-small": 12,
            "small": 28,
            "medium": 44,
            "large": 60,
            "extra-large": 76,
            "xx-large": 88,
        }
        return question_count_for_slug[quiz_size_slug]



class Answer(models.Model):

    """ Define a table in which to save each individual answer """

    quiz = models.ForeignKey('content.Quiz', on_delete=models.CASCADE)
    question_id = models.IntegerField(default=0)
    answer = models.IntegerField(default=0)

    def save_answer(self, quiz_id, question_id, answer):
        """ Save the quiz answers """
        # print('Answer - save_answer - question_id:', question_id)
        # print('Answer - save_answer - answer:', answer)
        self.quiz_id = quiz_id
        self.question_id = question_id
        self.answer = answer
        self.save()
        return self


class Score:

    """ Class to calculate, contain, and display the score for the quiz """

    def __init__(self):
        self.e_score = 0
        self.i_score = 0
        self.n_score = 0
        self.s_score = 0
        self.f_score = 0
        self.t_score = 0
        self.j_score = 0
        self.p_score = 0
        self.opposite_type = {
                "E": "I", "I": "E",
                "N": "S", "S": "N",
                "F": "T", "T": "F",
                "J": "P", "P": "J",
        }
        self.e_pct = None
        self.i_pct = None
        self.n_pct = None
        self.s_pct = None
        self.f_pct = None
        self.t_pct = None
        self.j_pct = None
        self.p_pct = None

    def tally_answer(self, answer_123_type, answer_int, answer_weight_int):

        """ Add the answer_weight to the appropriate score data member """

        if answer_int <= 3:
            type_for_answer = answer_123_type
        else:
            type_for_answer = self.opposite_type[answer_123_type]

        if type_for_answer is "E":
            self.e_score += answer_weight_int
        elif type_for_answer is "I":
            self.i_score += answer_weight_int
        elif type_for_answer is "N":
            self.n_score += answer_weight_int
        elif type_for_answer is "S":
            self.s_score += answer_weight_int
        elif type_for_answer is "F":
            self.f_score += answer_weight_int
        elif type_for_answer is "T":
            self.t_score += answer_weight_int
        elif type_for_answer is "J":
            self.j_score += answer_weight_int
        elif type_for_answer is "P":
            self.p_score += answer_weight_int

        if DJANGO_DEBUG:
            print('Score.tally_answer - added',
                str(answer_weight_int) + ' to '+ type_for_answer + ': ',
                self.__str__())

    def as_four_letter_type(self):
        """ Return a string containing the four letter type """
        four_letter_type = ''

        if self.i_score < self.e_score:
            four_letter_type += 'E'
        elif self.i_score == self.e_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'I'

        if self.s_score < self.n_score:
            four_letter_type += 'N'
        elif self.s_score == self.n_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'S'

        if self.t_score < self.f_score:
            four_letter_type += 'F'
        elif self.t_score == self.f_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'T'

        if self.p_score < self.j_score:
            four_letter_type += 'J'
        elif self.p_score == self.j_score:
            four_letter_type += 'X'
        else:
            four_letter_type += 'P'

        return four_letter_type

    def calculate_percentages(self):
        """ Calculate the percentages """
        total_ei_score = self.e_score + self.i_score
        total_ns_score = self.n_score + self.s_score
        total_ft_score = self.f_score + self.t_score
        total_jp_score = self.j_score + self.p_score

        if total_ei_score > 0:
            self.e_pct = round(100 * self.e_score / total_ei_score)
            self.i_pct = round(100 * self.i_score / total_ei_score)
        else:
            self.e_pct = 0
            self.i_pct = 0

        if total_ns_score > 0:
            self.n_pct = round(100 * self.n_score / total_ns_score)
            self.s_pct = round(100 * self.s_score / total_ns_score)
        else:
            self.n_pct = 0
            self.s_pct = 0

        if total_ft_score > 0:
            self.f_pct = round(100 * self.f_score / total_ft_score)
            self.t_pct = round(100 * self.t_score / total_ft_score)
        else:
            self.f_pct = 0
            self.t_pct = 0

        if total_jp_score > 0:
            self.j_pct = round(100 * self.j_score / total_jp_score)
            self.p_pct = round(100 * self.p_score / total_jp_score)
        else:
            self.j_pct = 0
            self.p_pct = 0

    def as_list_of_pcts_and_counts(self):
        """ Return a list containing both percentages and counts """
        if self.e_pct is None:
            self.calculate_percentages()

        score_list = [
            ['E: ' + str(self.e_pct) + '%&nbsp;(' + str(self.e_score) + ')',
             'I: ' + str(self.i_pct) + '%&nbsp;(' + str(self.i_score) + ')'],
            ['N: ' + str(self.n_pct) + '%&nbsp;(' + str(self.n_score) + ')',
             'S: ' + str(self.s_pct) + '%&nbsp;(' + str(self.s_score) + ')'],
            ['F: ' + str(self.f_pct) + '%&nbsp;(' + str(self.f_score) + ')',
             'T: ' + str(self.t_pct) + '%&nbsp;(' + str(self.t_score) + ')'],
            ['J: ' + str(self.j_pct) + '%&nbsp;(' + str(self.j_score) + ')',
             'P: ' + str(self.p_pct) + '%&nbsp;(' + str(self.p_score) + ')']
        ]
        return score_list

    def to_kv_pairs(self):
        """ Returns the current score as a list of key-value pairs """
        score = {
                "E": self.e_score,
                "I": self.i_score,
                "N": self.n_score,
                "S": self.s_score,
                "F": self.f_score,
                "T": self.t_score,
                "J": self.j_score,
                "P": self.p_score,
        }
        return score

    #
    # Reference for purpose of __str__() and __repl__():
    #   http://stackoverflow.com/questions/3691101/what-is-the-purpose-of-str-and-repr-in-python
    #

    def __repl__(self):
        return str(self.to_kv_pairs())

    def __str__(self):
        score_str  = 'E/I: ' + str(self.e_score) + '/' + str(self.i_score) + '; '
        score_str += 'N/S: ' + str(self.n_score) + '/' + str(self.s_score) + '; '
        score_str += 'F/T: ' + str(self.f_score) + '/' + str(self.t_score) + '; '
        score_str += 'J/P: ' + str(self.j_score) + '/' + str(self.p_score)
        return score_str


class QuizJson:

    """ Read in and work with all the questions in the entire quiz """


    def __init__(self):

        """ Populate the question_list with questions from the json file """

        self.question_list = self.read_quiz_json()

    def read_quiz_json(self):

        """ Read the quiz questions and answers from the json file """

        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        QUIZ_FILE_DIR = site_content_dir + '/static/content/json/quiz/'
        QUIZ_FILE_NAME = 'seeourminds_quiz.json'

        quiz_file_path = QUIZ_FILE_DIR + QUIZ_FILE_NAME
        quiz_json_file = open(quiz_file_path)
        quiz_json_string = quiz_json_file.read()
        quiz_json_file.close()
        question_list = json.loads(quiz_json_string)
        return(question_list)

    def get_quiz_question(self, question_int):

        """ Return the entire quiz question (answers, weights, etc.)"""

        quiz_question = self.question_list[question_int]
        # print('QuizJson.get_quiz_question - question_int:', question_int)
        # print('QuizJson.get_quiz_question - quiz_question:', quiz_question)
        return quiz_question

    def get_question_text(self, question_int):

        """ Get and return the question_text for the question """

        quiz_question = self.get_quiz_question(question_int)
        question_text = quiz_question['question_text']
        return question_text

    def get_choices(self, question_int):

        """ Return the answer choices for the given question """

        quiz_question = self.get_quiz_question(question_int)
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

        answer_7_text = quiz_question.get('answer_7_text')
        # print("answer_7_text:", answer_7_text)

        if answer_7_text is not None:
            choice_7 = ['7', answer_7_text]
            choices.append(choice_7)

        # print('QuizJson.get_choices - question_int:', question_int)
        # print('QuizJson.get_choices - len(choices):', len(choices))
        return choices

    def get_answer_123_type(self, question_int):

        """ Get and return the answer_123_type (e.g., "E") for the question """

        quiz_question = self.get_quiz_question(question_int)
        answer_123_type = quiz_question['answer_123_type']
        return answer_123_type

    def get_answer_text(self, question_int, answer_str):

        """ Get and return the answer_X_text for the selected answer 'X' """

        quiz_question = self.get_quiz_question(question_int)
        answer_text_key = "answer_" + answer_str + "_text"
        answer_text = quiz_question[answer_text_key]
        return answer_text

    def get_answer_weight(self, question_int, answer_str):

        """ Get and return the answer_X_weight for the selected answer 'X' """

        quiz_question = self.get_quiz_question(question_int)
        answer_weight_key = "answer_" + answer_str + "_weight"
        answer_weight = quiz_question[answer_weight_key]
        return answer_weight

    def print_cleaned_data(self, cleaned_data):
        """ print out the cleaned data, in order by question number """
        print('QuizJson.print_cleaned_data - cleaned_data:')

        for question_xx in sorted(cleaned_data):
            print('\tanswer for ' + question_xx + ': ' + cleaned_data[question_xx])

    def score_quiz(self, cleaned_data):

        """ Process the data from the form and set the scores """
        """ question_list is 0 based, the form questions are 1-based """

        # self.print_cleaned_data(cleaned_data)
        score = Score()

        for form_question_str in sorted(cleaned_data):
            if not form_question_str.startswith("question_"):
                continue
            question_int = int(form_question_str.replace("question_", ""))
            answer_123_type = self.get_answer_123_type(question_int)
            answer_str = cleaned_data[form_question_str]
            answer_int = int(answer_str)
            answer_weight_str = self.get_answer_weight(question_int, answer_str)
            answer_weight_int = int(answer_weight_str)
            if DJANGO_DEBUG:
                answer_text = self.get_answer_text(question_int, answer_str)
                question_text = self.get_question_text(question_int)
                print('QuizJson.score_quiz -',
                    str(question_int) + ' (' + answer_123_type + ')', '/',
                    str(answer_int) + ' (' + answer_weight_str + ')',
                    question_text, '/',
                    answer_text)
            score.tally_answer(answer_123_type, answer_int, answer_weight_int)

        return score
