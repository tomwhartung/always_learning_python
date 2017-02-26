#!/bin/bash
#
# Run the flask development server
#
export FLASK_DEBUG=1
##
## ** Trying to run the app using this technique (used on groja.com) causes a warning on bette:
##    "/usr/lib/python3.6/runpy.py:125: RuntimeWarning: 'flask.cli' found in sys.modules
##      after import of package 'flask', but prior to execution of 'flask.cli';
##       this may result in unpredictable behaviour"
## export FLASK_APP=groja.py
## python -m flask run
## python3 -m flask run
## ** Seriously wtf! **
##
python groja.py
