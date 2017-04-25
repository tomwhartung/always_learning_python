#!/bin/bash
#
# shell.sh: tiny shell script to enter the python server
#
# Sample commands:
# >>> from content.database import Answer
# >>> from content.database import Questionnaire
# >>> Answer.objects.all()
# >>> Questionnaire.objects.all()
# >>> quiz1 = Questionnaire.objects.get(pk=1)
# >>> ans1 = Answer.objects.get(pk=1)
# >>>
# >>>
# >>>
# >>>
#
#
export DJANGO_DEBUG=1
export RUNNING_LOCALLY=1
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage shell
