""" Contains the database models and access routines for our app.

Purpose: contains the methods for accessing and updating data in the database
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none, yet)
"""

import os
from django.db import models
from django.utils import timezone

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')

"""
There are 88 questions, and the ones I have the most confidence in are
nearer the beginning, with the "fun," experimental ones at the end.
It is desireable that the number of questions be divisible by 4 but not 8,
so that there is an odd number of questions for each pair of opposites.
"""
XX_SMALL = '2XS'       # 4 = 1*4 (for testing, keep off menu in production)
EXTRA_SMALL = 'XS'     # 12 = 3 * 4
SMALL = 'S'            # 28 = 7 * 4
MEDIUM = 'M'           # 44 = 11 * 4
LARGE = 'L'            # 60 = 15 * 4
EXTRA_LARGE = 'XL'     # 76 = 19 * 4
XX_LARGE = '2XL'       # 88 = 22 * 4


class Questionnaire(models.Model):

    """
    Define columns and save a person's questionnaire answers in the database.
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

    def save_questionnaire(self, cleaned_data, quiz_size_slug=DEFAULT_QUIZ_SIZE_SLUG):
        """
        If we have an email, save the questionnaire data, along with the answers
        There is no sense saving it if we do not have an email address!
        The check here may be redundant, but this is very important!
        Note also: the validation criteria for the db is stronger than
          it is for forms...!
        """
        email = cleaned_data['email']
        if len(email) < 4:    # "blank=False" does not seem to work?!?
            print('Questionnaire.save_questionnaire - not saving! email:', '"' + email + '"')
            return False
        else:
            name = cleaned_data['name']
            self.name = name
            self.email = email
            self.size = self.get_quiz_size_abbreviation_for_slug(quiz_size_slug)
            self.save()
            print('Questionnaire.save_questionnaire - saved name/email:', name + '/' + email)
            for form_question_str in sorted(cleaned_data):
                if not form_question_str.startswith("question_"):
                    continue
                question_int = int(form_question_str.replace("question_", ""))
                answer_str = cleaned_data[form_question_str]
                answer_int = int(answer_str)
                answer_db = Answer()
                answer_db.save_answer(self.id, question_int, answer_int)
        return self

    def load_answers(self, email):
        print('Questionnaire - load_answers(), email:', email)
        answers = {}
        return answers

    @classmethod
    def get_quiz_size_slugs_list(cls):
        """ Returns a list of the available quiz size choices """
        quiz_size_slugs = [
            'xx-small',
            'extra-small',
            'small',
            'medium',
            'large',
            'extra-large',
            'xx-large',
        ]
        return quiz_size_slugs

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

    @classmethod
    def get_quiz_size_text_for_slug(cls, quiz_size_slug):
        """ Returns the quiz size_text for the passed in quiz_size_slug """
        quiz_size_slugs_to_text = {
            'xx-small': '2X Small',
            'extra-small': 'Extra Small',
            'small': 'Small',
            'medium': 'Medium',
            'large': 'Large',
            'extra-large': 'Extra Large',
            'xx-large': '2X Large',
        }
        return quiz_size_slugs_to_text[quiz_size_slug]

    def __str__(self):
        name_email_size = self.name + '/' + self.email + '/' + self.size
        return name_email_size


class Answer(models.Model):

    """ Define a table in which to save each individual answer """

    questionnaire = models.ForeignKey('content.Questionnaire', on_delete=models.CASCADE)
    question_id = models.IntegerField(default=0)
    answer = models.IntegerField(default=0)

    def save_answer(self, questionnaire_id, question_id, answer):
        """ Save the questionnaire answers """
        # print('Answer - save_answer - question_id:', question_id)
        # print('Answer - save_answer - answer:', answer)
        self.questionnaire_id = questionnaire_id
        self.question_id = question_id
        self.answer = answer
        self.save()
        return self

    def __str__(self):
        question_id_answer = str(self.question_id) + '/' + str(self.answer)
        return question_id_answer
        # return 'answer: ' + str(self.answer)
