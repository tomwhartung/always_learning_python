##
#  When the visitor submits the form, send an email notification
#  Reference:
#     https://docs.python.org/3/library/email-examples.html
#
from flask import Flask, flash
from flask import redirect, render_template, request, session, url_for
from form import NameEmailForm
from db_access import update_or_insert_name_email
from send_email import send_interest_email

#  App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

##
#  Route for home page redirects to the form, making testing easier
#
@app.route( "/" )
def index():
   return redirect( url_for('contactme') )

##
#  Display contactme page with the form, and process it when it comes back
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
         ## insert_name_email( name, email, portrait=1 )
         update_or_insert_name_email( name, email, portrait=1 )
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
#  Thank the visitor for sharing their email address
#
@app.route( "/thanks" )
def thanks():
   name = session.get( 'name' )
   email = session.get( 'email' )
   ## send_interest_email( name + ' (' + email + ') has expressed an interest in buying a spiritual portrait!' )
   return render_template( 'thanks.html', name=name )

##
#  Run the app!
#
if __name__ == "__main__":
    app.run()
