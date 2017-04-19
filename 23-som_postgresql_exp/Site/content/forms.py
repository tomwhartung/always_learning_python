""" forms.py: forms used by the app

Purpose: populate the quiz page and implement the questionnaire
Author: Tom W. Hartung
Date: Spring, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:

"""

from django import forms
from .models import QuizJson


class QuizForm(forms.Form):

    """ The Quiz Form is a list of questions and multiple-choice answers """
    """ We are using the Brute Force Approach: """
    """ We tried several times to get this to work in a loop, to no avail """
    """ The failed attempts are labelled "Crufty" at the end of this file """

    def __init__(self, quiz_size="large", *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)

        quiz_size_counts = {
            "xx-small": 4,
            "extra-small": 12,
            "small": 28,
            "medium": 44,
            "large": 60,
            "extra-large": 76,
            "xx-large": 88,
        }
        quiz_json = QuizJson()
        question_count = quiz_size_counts[quiz_size]
        self.question_count = question_count
        print('QuizForm.__init__ - self.question_count:', self.question_count)

        self.fields['test1'] = forms.CharField(max_length=10, required=False)

        for question_no in range(0, question_count):
            question_key = 'question_' + str(question_no)
            print('question_no:', question_no)
            print('question_key:', question_key)
            radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
            label = quiz_json.get_label(question_no)
            choices = quiz_json.get_choices(question_no)
            self.fields[question_key] = forms.ChoiceField(
                widget=radio_widget, label=label, choices=choices
            )

    quiz_json = QuizJson()

    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)

def brute_force_questions():
    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label = quiz_json.get_label(0)
    choices = quiz_json.get_choices(0)
    question_01 = forms.ChoiceField(
            widget=radio_widget, label=label, choices=choices
    )

    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label = quiz_json.get_label(1)
    choices = quiz_json.get_choices(1)
    question_02 = forms.ChoiceField(
            widget=radio_widget, label=label, choices=choices
    )

    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label = quiz_json.get_label(2)
    choices = quiz_json.get_choices(2)
    question_03 = forms.ChoiceField(
            widget=radio_widget, label=label, choices=choices
    )

    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label = quiz_json.get_label(3)
    choices = quiz_json.get_choices(3)
    question_04 = forms.ChoiceField(
            widget=radio_widget, label=label, choices=choices
    )

    # def questions_05_thru_08():
    # """ SAVING THIS CODE FOR LATER """
    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(4)
    choices = quiz_json.get_choices(4)
    question_05 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(5)
    choices = quiz_json.get_choices(5)
    question_06 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(6)
    choices = quiz_json.get_choices(6)
    question_07 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(7)
    choices = quiz_json.get_choices(7)
    question_08 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    # def questions_09_thru_16():
    # """ SAVING THIS CODE FOR LATER """

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(8)
    choices = quiz_json.get_choices(8)
    question_09 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(9)
    choices = quiz_json.get_choices(9)
    question_10 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(10)
    choices = quiz_json.get_choices(10)
    question_11 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(11)
    choices = quiz_json.get_choices(11)
    question_12 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(12)
    choices = quiz_json.get_choices(12)
    question_13 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(13)
    choices = quiz_json.get_choices(13)
    question_14 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(14)
    choices = quiz_json.get_choices(14)
    question_15 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(15)
    choices = quiz_json.get_choices(15)
    question_16 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    # def questioins_17_thru_88():
    #     """ SAVING THIS CODE FOR LATER """

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(16)
    choices = quiz_json.get_choices(16)
    question_17 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(17)
    choices = quiz_json.get_choices(17)
    question_18 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(18)
    choices = quiz_json.get_choices(18)
    question_19 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(19)
    choices = quiz_json.get_choices(19)
    question_20 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(20)
    choices = quiz_json.get_choices(20)
    question_21 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(21)
    choices = quiz_json.get_choices(21)
    question_22 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(22)
    choices = quiz_json.get_choices(22)
    question_23 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(23)
    choices = quiz_json.get_choices(23)
    question_24 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(24)
    choices = quiz_json.get_choices(24)
    question_25 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(25)
    choices = quiz_json.get_choices(25)
    question_26 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(26)
    choices = quiz_json.get_choices(26)
    question_27 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(27)
    choices = quiz_json.get_choices(27)
    question_28 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(28)
    choices = quiz_json.get_choices(28)
    question_29 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(29)
    choices = quiz_json.get_choices(29)
    question_30 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(30)
    choices = quiz_json.get_choices(30)
    question_31 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(31)
    choices = quiz_json.get_choices(31)
    question_32 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(32)
    choices = quiz_json.get_choices(32)
    question_33 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(33)
    choices = quiz_json.get_choices(33)
    question_34 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(34)
    choices = quiz_json.get_choices(34)
    question_35 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(35)
    choices = quiz_json.get_choices(35)
    question_36 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(36)
    choices = quiz_json.get_choices(36)
    question_37 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(37)
    choices = quiz_json.get_choices(37)
    question_38 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(38)
    choices = quiz_json.get_choices(38)
    question_39 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(39)
    choices = quiz_json.get_choices(39)
    question_40 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(40)
    choices = quiz_json.get_choices(40)
    question_41 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(41)
    choices = quiz_json.get_choices(41)
    question_42 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(42)
    choices = quiz_json.get_choices(42)
    question_43 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(43)
    choices = quiz_json.get_choices(43)
    question_44 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(44)
    choices = quiz_json.get_choices(44)
    question_45 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(45)
    choices = quiz_json.get_choices(45)
    question_46 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(46)
    choices = quiz_json.get_choices(46)
    question_47 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(47)
    choices = quiz_json.get_choices(47)
    question_48 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(48)
    choices = quiz_json.get_choices(48)
    question_49 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(49)
    choices = quiz_json.get_choices(49)
    question_50 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(50)
    choices = quiz_json.get_choices(50)
    question_51 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(51)
    choices = quiz_json.get_choices(51)
    question_52 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(52)
    choices = quiz_json.get_choices(52)
    question_53 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(53)
    choices = quiz_json.get_choices(53)
    question_54 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(54)
    choices = quiz_json.get_choices(54)
    question_55 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(55)
    choices = quiz_json.get_choices(55)
    question_56 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(56)
    choices = quiz_json.get_choices(56)
    question_57 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(57)
    choices = quiz_json.get_choices(57)
    question_58 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(58)
    choices = quiz_json.get_choices(58)
    question_59 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(59)
    choices = quiz_json.get_choices(59)
    question_60 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(60)
    choices = quiz_json.get_choices(60)
    question_61 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(61)
    choices = quiz_json.get_choices(61)
    question_62 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(62)
    choices = quiz_json.get_choices(62)
    question_63 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(63)
    choices = quiz_json.get_choices(63)
    question_64 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(64)
    choices = quiz_json.get_choices(64)
    question_65 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(65)
    choices = quiz_json.get_choices(65)
    question_66 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(66)
    choices = quiz_json.get_choices(66)
    question_67 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(67)
    choices = quiz_json.get_choices(67)
    question_68 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(68)
    choices = quiz_json.get_choices(68)
    question_69 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(69)
    choices = quiz_json.get_choices(69)
    question_70 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(70)
    choices = quiz_json.get_choices(70)
    question_71 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(71)
    choices = quiz_json.get_choices(71)
    question_72 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(72)
    choices = quiz_json.get_choices(72)
    question_73 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(73)
    choices = quiz_json.get_choices(73)
    question_74 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(74)
    choices = quiz_json.get_choices(74)
    question_75 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(75)
    choices = quiz_json.get_choices(75)
    question_76 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(76)
    choices = quiz_json.get_choices(76)
    question_77 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(77)
    choices = quiz_json.get_choices(77)
    question_78 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(78)
    choices = quiz_json.get_choices(78)
    question_79 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(79)
    choices = quiz_json.get_choices(79)
    question_80 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(80)
    choices = quiz_json.get_choices(80)
    question_81 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(81)
    choices = quiz_json.get_choices(81)
    question_82 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(82)
    choices = quiz_json.get_choices(82)
    question_83 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(83)
    choices = quiz_json.get_choices(83)
    question_84 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(84)
    choices = quiz_json.get_choices(84)
    question_85 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(85)
    choices = quiz_json.get_choices(85)
    question_86 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(86)
    choices = quiz_json.get_choices(86)
    question_87 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label = quiz_json.get_label(87)
    choices = quiz_json.get_choices(87)
    question_88 = forms.ChoiceField( widget=radio_widget, label=label, choices=choices )


#
# *******************************
# *** CRUFTY CODE STARTS HERE ***
# *******************************
#


def try_using_a_loop():

    """ CRUFT ALERT: Saving this code for possible future reference """
    """ Tried using a loop to populate the questions, but it didn't work  """
    """ We always get only one question (the last one) """
    """ Saving this code in case we want to try again ... """

    radio_widgets = []
    question_inputs = []

    for question_no in range(0, 6):
        this_radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
        radio_widgets.insert(question_no, this_radio_widget)
        label = quiz_json.get_label(question_no)
        choices = quiz_json.get_choices(question_no)
        this_question_input = forms.ChoiceField(
                widget=radio_widgets[question_no], label=label, choices=choices
        )
        question_inputs.insert(question_no, this_question_input)
        print('question_no:', question_no)
        print('len(radio_widgets):', len(radio_widgets))
        print('len(question_inputs):', len(question_inputs))


def try_using_a_loop_in_init(self):

    """ CRUFT ALERT: Saving this code for possible future reference """
    """ Tried using a loop to populate the questions, but it didn't work  """

    self.quiz_json = QuizJson()
    self.question_inputs = [0] * 88

    for question_no in range(0, 6):
        radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
        label = self.quiz_json.get_label(question_no)
        choices = self.quiz_json.get_choices(question_no)
        self.question_inputs[question_no] = forms.ChoiceField(
                widget=radio_widget, label=label, choices=choices
        )
        print('question_no:', question_no)
        # print('len(radio_widgets):', len(radio_widgets))
        print('len(self.question_inputs):', len(self.question_inputs))


def try_using_a_loop_closest_so_far():

    """ CRUFT ALERT: Saving this code for possible future reference """
    """ Tried using a loop to populate the questions, but it didn't work  """
    """ This one runs without error but does not show any input fields """

    question_inputs = [0] * 88

    for question_no in range(0, 6):
        radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
        label = quiz_json.get_label(question_no)
        choices = quiz_json.get_choices(question_no)
        question_inputs[question_no] = forms.ChoiceField(
                widget=radio_widget, label=label, choices=choices
        )
        print('question_no:', question_no)
        # print('len(radio_widgets):', len(radio_widgets))
        print('len(question_inputs):', len(question_inputs))
