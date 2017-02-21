##
#  Create a form to get the visitor's name and email address
#  Reference:
#     https://pythonspot.com/flask-web-forms/
#
from flask import Flask, flash
from flask import redirect, render_template, request, session, url_for
from form import NameEmailForm

#  App config.
DEBUG = True
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
      print( "name: ", name, "email: ", email )

      if form.validate():
         session['name'] = name
         flash( 'Thanks, we will be in touch with you soon!' )
         return redirect( url_for('thanks') )
      else:
         print( "form.errors:", form.errors )
         #
         #  key = 'email', values = list of error messages
         ## flash( form.errors )
         #
         for key, value in form.errors.items():
            for message in value:
               flash( message )

   return render_template( 'contactme.html', form=form )

##
# Thank the visitor for sharing their email address
#
@app.route( "/thanks" )
def thanks():
   name = session.get( 'name' )
   return render_template( 'thanks.html', name=name )


if __name__ == "__main__":
    app.run()
