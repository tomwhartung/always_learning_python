
##
# From Chapter 2 of Flas Web Development
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
# Second, we personalize the message
# This is called a "dynamic route"
#
@app.route( '/user/<name>' )
def user( name ) :
   return '<h3>Hi there, %s!</h3><p>Who\'s in charge around here?</p>' % name

if __name__ == '__main__' :
   app.run( debug=True )

