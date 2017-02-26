##
# hello.py from Chapter 6 of Flask Web Development
# ------------------------------------------------
#
from flask import Flask
app = Flask( __name__ )

import os
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

##
# First, we say hello.
#
@app.route( '/' )
def index() :
   return '<h3>Hi there, earthling!</h3><p>Take me to your leader!</p>'

## ##
## # Run the app!
## #
## if __name__ == '__main__' :
##    app.run( debug=True )

