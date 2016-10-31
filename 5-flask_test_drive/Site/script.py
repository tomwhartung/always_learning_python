
##
# From Chapter 2 of the "Flask Web Development" book
# --------------------------------------------------
#
# Using hello.py as a starting point, add in Flask-Script and
# test drive that.
#
from flask import Flask
from flask.ext.script import Manager

app = Flask( __name__ )
manager = Manager( app )

##
# Personalize the message
# This is called a "dynamic route"
#
@app.route( '/user/<name>' )
def user( name ) :
   return '<h3>Hi there, %s!</h3><p>Who\'s in charge around here?</p>' % name

##
# Can we accesss the host or port or both?
# Surely we can, but how?
#
@app.route( '/' )
def index() :
   ## host = manager.host
   host = ''

   if( host == '' ) :
      host = '???'
   return '<h3>Hi</h3><p>The host is "%s" .</p>' % host

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

