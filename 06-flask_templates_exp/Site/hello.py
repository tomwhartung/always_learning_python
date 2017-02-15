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
   return render_template( 'base.html' )

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

