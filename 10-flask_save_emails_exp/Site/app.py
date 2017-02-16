##
# Save contact me email addresses in an sqlite3 db
# ------------------------------------------------
#
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask( __name__ )
app.config['SECRET_KEY'] = 'AbcdefGhijklmNopqrstuVwxyz'

##
# Define the form
#
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameEmailForm(Form):
    name = StringField( 'Name', validators=[Required()] )
    email = StringField( 'Email', validators=[Required(), Email()] )
    submit = SubmitField( 'Get Your Portrait' )

##
# Display the wtf index form
#
@app.route( '/', methods=['GET', 'POST'] )
def index() :
   name = None
   email = None
   form = NameEmailForm()
   if form.validate_on_submit():
      name = form.name.data
      form.name.data = ''
   return render_template('index.html', form=form, name=name)

##
# Display the contactme form
#
@app.route( '/contactme' )
def contactme() :
   return render_template( 'contactme.html' )

##
# Run the app!
#
if __name__ == '__main__' :
   app.run( debug=True )

