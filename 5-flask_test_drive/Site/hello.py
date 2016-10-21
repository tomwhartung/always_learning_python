
##
# From Chapter 2 of Flas Web Development
#
from flask import Flask
app = Flask( __name__ )

@app.route( '/' )
def index() :
   return '<h3>Hi there, earthling!</h3><p>Take me to your leader!</p>'

if __name__ == '__main__' :
   app.run( debug=True )

