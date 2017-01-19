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
# Show the Home page:
#
@app.route( '/' )
def index() :
   return render_template( 'home.html' )

##
# Show the About page:
#
@app.route( '/about' )
def about() :
   return render_template( 'about.html' )

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

