##
# Save contact me email addresses in an sqlite3 db
# ------------------------------------------------
#
from flask import Flask, render_template
app = Flask( __name__ )

##
# Display the form
#
@app.route( '/' )
def index() :
   return render_template( 'contactme.html' )

##
# Process the form
#
@app.route( '/save_email' )
def save_email() :
   return '<h3>Success</h3><p>email address saved ok</p>'

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

