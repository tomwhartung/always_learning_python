##
# Save contact me email addresses in an sqlite3 db
# ------------------------------------------------
# This is kind of an amalgamation of two tutorials.
# References:
#   https://www.tutorialspoint.com/flask/flask_wtf.htm
#   http://flask.pocoo.org/docs/0.12/patterns/wtforms/
#
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask( __name__ )
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'AbcdefGhijklmNopqrstuVwxyz'

##
# Define the form
#
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators, ValidationError
from wtforms.validators import Required, Email

class MyNameEmailForm(FlaskForm):
    name = StringField( 'Name', validators=[Required()] )
    email = StringField( 'Email',
       [ validators.Required("Please share your email address so that we can contact you."),
         validators.Email("Please enter a valid email address.")] )
    submit = SubmitField( 'Get Your Portrait' )

##
# Display the wtf index form
#
@app.route( '/', methods=['GET', 'POST'] )
def index() :
   name = None
   email = None
   form = MyNameEmailForm()
   if request.method == 'POST':
      if form.validate_on_submit():
         return render_template('thanks.html', name=name, email=email)
      else:
         name = form.name.data
         email = form.email.data
         return render_template('index.html', form=form, name=name, email=email)
   else:
      name = form.name.data
      form.name.data = ''
      email = form.email.data
      form.email.data = ''
      return render_template('index.html', form=form, name=name, email=email)

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
