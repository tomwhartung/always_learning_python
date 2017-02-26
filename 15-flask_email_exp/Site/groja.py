##
#  Create a form to get the visitor's name and email address
#  Reference:
#     https://pythonspot.com/flask-web-forms/
#
from flask import Flask, flash
from flask import redirect, render_template, request, session, url_for
from form import NameEmailForm
from db_access import insert_name_email

#  App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

##
# Route for home page redirects to the form, making testing easier
#
@app.route( "/" )
def index():
   return redirect( url_for('contactme') )

##
# Display contactme page with the form, and process it when it comes back
#
@app.route("/contactme", methods=['GET', 'POST'])
def contactme():
   form = NameEmailForm( request.form )

   if request.method == 'POST':
      name = form.name.data
      email = form.email.data

      if form.validate():
         session['name'] = name
         session['email'] = email
         insert_name_email( name, email, portrait=1 )
         flash( 'Thanks, we will be in touch with you soon!' )
         return redirect( url_for('thanks') )
      else:
         ## print( "form.errors:", form.errors )
         #
         #  key = 'email', values = [] (list of error messages)
         #
         for key, value in form.errors.items():
            for message in value:
               flash( message )
   else:
      form.name.data = ''
      form.email.data = ''

   return render_template( 'contactme.html', form=form )

##
# Thank the visitor for sharing their email address
#
@app.route( "/thanks" )
def thanks():
   name = session.get( 'name' )
   email = session.get( 'email' )
   send_test_email( name + ' (' + email + ') has expressed an interest in buying a spiritual portrait!' )
   return render_template( 'thanks.html', name=name )

##
#  First: send a simple test email
#
import os
from flask_mail import Mail
from flask_mail import Message
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_FROM'] = 'no_reply@tomhartung.com'
app.config['MAIL_TO'] = 'tomwhartung@tmail.com'
mail = Mail(app)
def send_test_email( message_text ):
   print( 'In the send_test_email() in groja.py, message_text =', message_text )
   message = Message(
      'Interest in a spiritual portrait',
      sender=app.config['MAIL_FROM'],
      recipients=[app.config['MAIL_TO']] )
   message.body = message_text
   message.html = ''
   mail.send( message )
   return True

##
#  Run the app!
#
if __name__ == "__main__":
    app.run()
