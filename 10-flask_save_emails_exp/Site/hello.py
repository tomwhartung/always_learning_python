##
# Std hello world sanity check
# ----------------------------
#
from flask import Flask
app = Flask( __name__ )

##
# First, we say hello.
#
@app.route( '/' )
def index() :
   return '<h3>Hi there, earthling!</h3><p>Take me to your leader!</p>'

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

