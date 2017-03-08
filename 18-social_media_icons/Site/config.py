##
# Flask configuration for groja.com
# ---------------------------------
# After a bit of research, we are going to use the method presented here:
#   http://flask.pocoo.org/docs/0.11/config/
# Another resource:
#   https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
#
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config( object ):
   TEMPLATES_AUTO_RELOAD = True
   SEND_FILE_MAX_AGE_DEFAULT = 0
   CSRF_ENABLED = True
   #
   #  This is just a formality, to insure the DEBUG setting is off in production.
   #  We turn on debugging by setting FLASK_DEBUG to 1 in the run.sh script
   #
   DEBUG = False
   #
   #  Reference: http://flask.pocoo.org/docs/0.12/quickstart/#sessions
   #
   SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz'

