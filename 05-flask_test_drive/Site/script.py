
##
# From Chapter 2 of the "Flask Web Development" book
# --------------------------------------------------
#
# Using hello.py as a starting point, add in Flask-Script and
# test drive that.
#
# Notes:
# 1) We now create a Manager object and use it to run the app
#    -> See last lines in this file
# 2) We get the host and port from the request object
#
from flask import Flask
from flask_script import Manager

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
# Display the host and port
#
from flask import request
@app.route( '/' )
def index() :
   host = request.host
   return '<h3>Hi</h3><p>The request.host is "%s" .</p>' % request.host

##
# Run the app!
#
if __name__ == '__main__' :
   ## app.run( debug=True )
   manager.run()

