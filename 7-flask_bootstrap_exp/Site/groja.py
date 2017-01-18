##
# From Chapter 3 of the "Flask Web Development" book
# --------------------------------------------------
#
# Experimenting with templates
#
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask( __name__ )
Bootstrap( app )

##
# Use a template to show a Home page
#
@app.route( '/' )
def index() :
   return render_template( 'home.html' )

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

