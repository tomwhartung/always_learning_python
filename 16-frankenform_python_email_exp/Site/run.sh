#!/bin/bash
#
# Run the flask development server
#
rm -f *.pyc 2>/dev/null
## #
## #  We'd like to be able to run it like we run groja.com ...
## #
## export FLASK_APP=groja.py
## python -m flask run
## python3 -m flask run
##
export FLASK_DEBUG=1
python groja.py
