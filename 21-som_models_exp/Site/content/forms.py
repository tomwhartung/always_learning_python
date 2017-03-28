""" forms.py: forms used by the app

Purpose: populate the quiz page and implement the questionnaire
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:

"""

from django import forms
from .models import Quiz


class QuizForm(forms.Form):

    """ Convert our json to a list of questions and multiple-choice answers """

    def get_label(question_no, quiz_question):

        """ Get and return the question_text ("label") for the question """

        # print('get_label - question_no:', question_no)
        # print('get_label - quiz_question:', quiz_question)
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

    # name = forms.CharField(max_length=50)
    # email = forms.EmailField()

    my_quiz = Quiz()
    quiz_dictionary = my_quiz.read_quiz_json()

    # print('quiz_dictionary:', quiz_dictionary)
    # print('len(quiz_dictionary):', len(quiz_dictionary))
    # print('quiz_dictionary[0]:', quiz_dictionary[0])
    print('my_quiz.get_quiz_question(0):', my_quiz.get_quiz_question(0))

    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label_01 = my_quiz.get_label(0)
    choices_01 = my_quiz.get_choices(0)
    question_01 = forms.ChoiceField(
            widget=radio_widget, label=label_01, choices=choices_01
    )

    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label_02 = my_quiz.get_label(1)
    choices_02 = my_quiz.get_choices(1)
    question_02 = forms.ChoiceField(
            widget=radio_widget, label=label_02, choices=choices_02
    )

    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label_03 = my_quiz.get_label(2)
    choices_03 = my_quiz.get_choices(2)
    question_03 = forms.ChoiceField(
            widget=radio_widget, label=label_03, choices=choices_03
    )

    radio_widget = forms.RadioSelect(attrs={'class': 'quiz_answer'})
    label_04 = my_quiz.get_label(3)
    choices_04 = my_quiz.get_choices(3)
    question_04 = forms.ChoiceField(
            widget=radio_widget, label=label_04, choices=choices_04
    )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_05 = my_quiz.get_label(4)
    choices_05 = my_quiz.get_choices(4)
    question_05 = forms.ChoiceField( widget=radio_widget, label=label_05, choices=choices_05 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_06 = my_quiz.get_label(5)
    choices_06 = my_quiz.get_choices(5)
    question_06 = forms.ChoiceField( widget=radio_widget, label=label_06, choices=choices_06 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_07 = my_quiz.get_label(6)
    choices_07 = my_quiz.get_choices(6)
    question_07 = forms.ChoiceField( widget=radio_widget, label=label_07, choices=choices_07 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_08 = my_quiz.get_label(7)
    choices_08 = my_quiz.get_choices(7)
    question_08 = forms.ChoiceField( widget=radio_widget, label=label_08, choices=choices_08 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_09 = my_quiz.get_label(8)
    choices_09 = my_quiz.get_choices(8)
    question_09 = forms.ChoiceField( widget=radio_widget, label=label_09, choices=choices_09 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_10 = my_quiz.get_label(9)
    choices_10 = my_quiz.get_choices(9)
    question_10 = forms.ChoiceField( widget=radio_widget, label=label_10, choices=choices_10 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_11 = my_quiz.get_label(10)
    choices_11 = my_quiz.get_choices(10)
    question_11 = forms.ChoiceField( widget=radio_widget, label=label_11, choices=choices_11 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_12 = my_quiz.get_label(11)
    choices_12 = my_quiz.get_choices(11)
    question_12 = forms.ChoiceField( widget=radio_widget, label=label_12, choices=choices_12 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_13 = my_quiz.get_label(12)
    choices_13 = my_quiz.get_choices(12)
    question_13 = forms.ChoiceField( widget=radio_widget, label=label_13, choices=choices_13 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_14 = my_quiz.get_label(13)
    choices_14 = my_quiz.get_choices(13)
    question_14 = forms.ChoiceField( widget=radio_widget, label=label_14, choices=choices_14 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_15 = my_quiz.get_label(14)
    choices_15 = my_quiz.get_choices(14)
    question_15 = forms.ChoiceField( widget=radio_widget, label=label_15, choices=choices_15 )

    radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
    label_16 = my_quiz.get_label(15)
    choices_16 = my_quiz.get_choices(15)
    question_16 = forms.ChoiceField( widget=radio_widget, label=label_16, choices=choices_16 )


    def code_for_later():

        """ SAVING THIS CODE FOR LATER """

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_17 = my_quiz.get_label(16)
        choices_17 = my_quiz.get_choices(16)
        question_17 = forms.ChoiceField( widget=radio_widget, label=label_17, choices=choices_17 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_18 = my_quiz.get_label(17)
        choices_18 = my_quiz.get_choices(17)
        question_18 = forms.ChoiceField( widget=radio_widget, label=label_18, choices=choices_18 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_19 = my_quiz.get_label(18)
        choices_19 = my_quiz.get_choices(18)
        question_19 = forms.ChoiceField( widget=radio_widget, label=label_19, choices=choices_19 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_20 = my_quiz.get_label(19)
        choices_20 = my_quiz.get_choices(19)
        question_20 = forms.ChoiceField( widget=radio_widget, label=label_20, choices=choices_20 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_21 = my_quiz.get_label(20)
        choices_21 = my_quiz.get_choices(20)
        question_21 = forms.ChoiceField( widget=radio_widget, label=label_21, choices=choices_21 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_22 = my_quiz.get_label(21)
        choices_22 = my_quiz.get_choices(21)
        question_22 = forms.ChoiceField( widget=radio_widget, label=label_22, choices=choices_22 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_23 = my_quiz.get_label(22)
        choices_23 = my_quiz.get_choices(22)
        question_23 = forms.ChoiceField( widget=radio_widget, label=label_23, choices=choices_23 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_24 = my_quiz.get_label(23)
        choices_24 = my_quiz.get_choices(23)
        question_24 = forms.ChoiceField( widget=radio_widget, label=label_24, choices=choices_24 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_25 = my_quiz.get_label(24)
        choices_25 = my_quiz.get_choices(24)
        question_25 = forms.ChoiceField( widget=radio_widget, label=label_25, choices=choices_25 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_26 = my_quiz.get_label(25)
        choices_26 = my_quiz.get_choices(25)
        question_26 = forms.ChoiceField( widget=radio_widget, label=label_26, choices=choices_26 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_27 = my_quiz.get_label(26)
        choices_27 = my_quiz.get_choices(26)
        question_27 = forms.ChoiceField( widget=radio_widget, label=label_27, choices=choices_27 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_28 = my_quiz.get_label(27)
        choices_28 = my_quiz.get_choices(27)
        question_28 = forms.ChoiceField( widget=radio_widget, label=label_28, choices=choices_28 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_29 = my_quiz.get_label(28)
        choices_29 = my_quiz.get_choices(28)
        question_29 = forms.ChoiceField( widget=radio_widget, label=label_29, choices=choices_29 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_30 = my_quiz.get_label(29)
        choices_30 = my_quiz.get_choices(29)
        question_30 = forms.ChoiceField( widget=radio_widget, label=label_30, choices=choices_30 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_31 = my_quiz.get_label(30)
        choices_31 = my_quiz.get_choices(30)
        question_31 = forms.ChoiceField( widget=radio_widget, label=label_31, choices=choices_31 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_32 = my_quiz.get_label(31)
        choices_32 = my_quiz.get_choices(31)
        question_32 = forms.ChoiceField( widget=radio_widget, label=label_32, choices=choices_32 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_33 = my_quiz.get_label(32)
        choices_33 = my_quiz.get_choices(32)
        question_33 = forms.ChoiceField( widget=radio_widget, label=label_33, choices=choices_33 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_34 = my_quiz.get_label(33)
        choices_34 = my_quiz.get_choices(33)
        question_34 = forms.ChoiceField( widget=radio_widget, label=label_34, choices=choices_34 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_35 = my_quiz.get_label(34)
        choices_35 = my_quiz.get_choices(34)
        question_35 = forms.ChoiceField( widget=radio_widget, label=label_35, choices=choices_35 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_36 = my_quiz.get_label(35)
        choices_36 = my_quiz.get_choices(35)
        question_36 = forms.ChoiceField( widget=radio_widget, label=label_36, choices=choices_36 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_37 = my_quiz.get_label(36)
        choices_37 = my_quiz.get_choices(36)
        question_37 = forms.ChoiceField( widget=radio_widget, label=label_37, choices=choices_37 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_38 = my_quiz.get_label(37)
        choices_38 = my_quiz.get_choices(37)
        question_38 = forms.ChoiceField( widget=radio_widget, label=label_38, choices=choices_38 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_39 = my_quiz.get_label(38)
        choices_39 = my_quiz.get_choices(38)
        question_39 = forms.ChoiceField( widget=radio_widget, label=label_39, choices=choices_39 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_40 = my_quiz.get_label(39)
        choices_40 = my_quiz.get_choices(39)
        question_40 = forms.ChoiceField( widget=radio_widget, label=label_40, choices=choices_40 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_41 = my_quiz.get_label(40)
        choices_41 = my_quiz.get_choices(40)
        question_41 = forms.ChoiceField( widget=radio_widget, label=label_41, choices=choices_41 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_42 = my_quiz.get_label(41)
        choices_42 = my_quiz.get_choices(41)
        question_42 = forms.ChoiceField( widget=radio_widget, label=label_42, choices=choices_42 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_43 = my_quiz.get_label(42)
        choices_43 = my_quiz.get_choices(42)
        question_43 = forms.ChoiceField( widget=radio_widget, label=label_43, choices=choices_43 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_44 = my_quiz.get_label(43)
        choices_44 = my_quiz.get_choices(43)
        question_44 = forms.ChoiceField( widget=radio_widget, label=label_44, choices=choices_44 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_45 = my_quiz.get_label(44)
        choices_45 = my_quiz.get_choices(44)
        question_45 = forms.ChoiceField( widget=radio_widget, label=label_45, choices=choices_45 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_46 = my_quiz.get_label(45)
        choices_46 = my_quiz.get_choices(45)
        question_46 = forms.ChoiceField( widget=radio_widget, label=label_46, choices=choices_46 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_47 = my_quiz.get_label(46)
        choices_47 = my_quiz.get_choices(46)
        question_47 = forms.ChoiceField( widget=radio_widget, label=label_47, choices=choices_47 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_48 = my_quiz.get_label(47)
        choices_48 = my_quiz.get_choices(47)
        question_48 = forms.ChoiceField( widget=radio_widget, label=label_48, choices=choices_48 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_49 = my_quiz.get_label(48)
        choices_49 = my_quiz.get_choices(48)
        question_49 = forms.ChoiceField( widget=radio_widget, label=label_49, choices=choices_49 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_50 = my_quiz.get_label(49)
        choices_50 = my_quiz.get_choices(49)
        question_50 = forms.ChoiceField( widget=radio_widget, label=label_50, choices=choices_50 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_51 = my_quiz.get_label(50)
        choices_51 = my_quiz.get_choices(50)
        question_51 = forms.ChoiceField( widget=radio_widget, label=label_51, choices=choices_51 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_52 = my_quiz.get_label(51)
        choices_52 = my_quiz.get_choices(51)
        question_52 = forms.ChoiceField( widget=radio_widget, label=label_52, choices=choices_52 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_53 = my_quiz.get_label(52)
        choices_53 = my_quiz.get_choices(52)
        question_53 = forms.ChoiceField( widget=radio_widget, label=label_53, choices=choices_53 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_54 = my_quiz.get_label(53)
        choices_54 = my_quiz.get_choices(53)
        question_54 = forms.ChoiceField( widget=radio_widget, label=label_54, choices=choices_54 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_55 = my_quiz.get_label(54)
        choices_55 = my_quiz.get_choices(54)
        question_55 = forms.ChoiceField( widget=radio_widget, label=label_55, choices=choices_55 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_56 = my_quiz.get_label(55)
        choices_56 = my_quiz.get_choices(55)
        question_56 = forms.ChoiceField( widget=radio_widget, label=label_56, choices=choices_56 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_57 = my_quiz.get_label(56)
        choices_57 = my_quiz.get_choices(56)
        question_57 = forms.ChoiceField( widget=radio_widget, label=label_57, choices=choices_57 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_58 = my_quiz.get_label(57)
        choices_58 = my_quiz.get_choices(57)
        question_58 = forms.ChoiceField( widget=radio_widget, label=label_58, choices=choices_58 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_59 = my_quiz.get_label(58)
        choices_59 = my_quiz.get_choices(58)
        question_59 = forms.ChoiceField( widget=radio_widget, label=label_59, choices=choices_59 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_60 = my_quiz.get_label(59)
        choices_60 = my_quiz.get_choices(59)
        question_60 = forms.ChoiceField( widget=radio_widget, label=label_60, choices=choices_60 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_61 = my_quiz.get_label(60)
        choices_61 = my_quiz.get_choices(60)
        question_61 = forms.ChoiceField( widget=radio_widget, label=label_61, choices=choices_61 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_62 = my_quiz.get_label(61)
        choices_62 = my_quiz.get_choices(61)
        question_62 = forms.ChoiceField( widget=radio_widget, label=label_62, choices=choices_62 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_63 = my_quiz.get_label(62)
        choices_63 = my_quiz.get_choices(62)
        question_63 = forms.ChoiceField( widget=radio_widget, label=label_63, choices=choices_63 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_64 = my_quiz.get_label(63)
        choices_64 = my_quiz.get_choices(63)
        question_64 = forms.ChoiceField( widget=radio_widget, label=label_64, choices=choices_64 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_65 = my_quiz.get_label(64)
        choices_65 = my_quiz.get_choices(64)
        question_65 = forms.ChoiceField( widget=radio_widget, label=label_65, choices=choices_65 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_66 = my_quiz.get_label(65)
        choices_66 = my_quiz.get_choices(65)
        question_66 = forms.ChoiceField( widget=radio_widget, label=label_66, choices=choices_66 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_67 = my_quiz.get_label(66)
        choices_67 = my_quiz.get_choices(66)
        question_67 = forms.ChoiceField( widget=radio_widget, label=label_67, choices=choices_67 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_68 = my_quiz.get_label(67)
        choices_68 = my_quiz.get_choices(67)
        question_68 = forms.ChoiceField( widget=radio_widget, label=label_68, choices=choices_68 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_69 = my_quiz.get_label(68)
        choices_69 = my_quiz.get_choices(68)
        question_69 = forms.ChoiceField( widget=radio_widget, label=label_69, choices=choices_69 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_70 = my_quiz.get_label(69)
        choices_70 = my_quiz.get_choices(69)
        question_70 = forms.ChoiceField( widget=radio_widget, label=label_70, choices=choices_70 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_71 = my_quiz.get_label(70)
        choices_71 = my_quiz.get_choices(70)
        question_71 = forms.ChoiceField( widget=radio_widget, label=label_71, choices=choices_71 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_72 = my_quiz.get_label(71)
        choices_72 = my_quiz.get_choices(71)
        question_72 = forms.ChoiceField( widget=radio_widget, label=label_72, choices=choices_72 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_73 = my_quiz.get_label(72)
        choices_73 = my_quiz.get_choices(72)
        question_73 = forms.ChoiceField( widget=radio_widget, label=label_73, choices=choices_73 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_74 = my_quiz.get_label(73)
        choices_74 = my_quiz.get_choices(73)
        question_74 = forms.ChoiceField( widget=radio_widget, label=label_74, choices=choices_74 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_75 = my_quiz.get_label(74)
        choices_75 = my_quiz.get_choices(74)
        question_75 = forms.ChoiceField( widget=radio_widget, label=label_75, choices=choices_75 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_76 = my_quiz.get_label(75)
        choices_76 = my_quiz.get_choices(75)
        question_76 = forms.ChoiceField( widget=radio_widget, label=label_76, choices=choices_76 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_77 = my_quiz.get_label(76)
        choices_77 = my_quiz.get_choices(76)
        question_77 = forms.ChoiceField( widget=radio_widget, label=label_77, choices=choices_77 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_78 = my_quiz.get_label(77)
        choices_78 = my_quiz.get_choices(77)
        question_78 = forms.ChoiceField( widget=radio_widget, label=label_78, choices=choices_78 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_79 = my_quiz.get_label(78)
        choices_79 = my_quiz.get_choices(78)
        question_79 = forms.ChoiceField( widget=radio_widget, label=label_79, choices=choices_79 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_80 = my_quiz.get_label(79)
        choices_80 = my_quiz.get_choices(79)
        question_80 = forms.ChoiceField( widget=radio_widget, label=label_80, choices=choices_80 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_81 = my_quiz.get_label(80)
        choices_81 = my_quiz.get_choices(80)
        question_81 = forms.ChoiceField( widget=radio_widget, label=label_81, choices=choices_81 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_82 = my_quiz.get_label(81)
        choices_82 = my_quiz.get_choices(81)
        question_82 = forms.ChoiceField( widget=radio_widget, label=label_82, choices=choices_82 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_83 = my_quiz.get_label(82)
        choices_83 = my_quiz.get_choices(82)
        question_83 = forms.ChoiceField( widget=radio_widget, label=label_83, choices=choices_83 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_84 = my_quiz.get_label(83)
        choices_84 = my_quiz.get_choices(83)
        question_84 = forms.ChoiceField( widget=radio_widget, label=label_84, choices=choices_84 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_85 = my_quiz.get_label(84)
        choices_85 = my_quiz.get_choices(84)
        question_85 = forms.ChoiceField( widget=radio_widget, label=label_85, choices=choices_85 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_86 = my_quiz.get_label(85)
        choices_86 = my_quiz.get_choices(85)
        question_86 = forms.ChoiceField( widget=radio_widget, label=label_86, choices=choices_86 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_87 = my_quiz.get_label(86)
        choices_87 = my_quiz.get_choices(86)
        question_87 = forms.ChoiceField( widget=radio_widget, label=label_87, choices=choices_87 )

        radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
        label_88 = my_quiz.get_label(87)
        choices_88 = my_quiz.get_choices(87)
        question_88 = forms.ChoiceField( widget=radio_widget, label=label_88, choices=choices_88 )
