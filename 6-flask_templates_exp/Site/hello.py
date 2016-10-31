##
# From Chapter 3 of the "Flask Web Development" book
# --------------------------------------------------
#
# Experimenting with templates
#
from flask import Flask, render_template
app = Flask( __name__ )

##
# Use a template to say hello.
#
@app.route( '/' )
def index() :
   return render_template( 'index.html' )

##
# Allow for personalizing the message
#
@app.route( '/user/<name>' )
def user( name ) :
   return '<h3>Hi there, %s!</h3><p>Sorry this is not yet in a template.  Baby steps!</p>' % name

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

