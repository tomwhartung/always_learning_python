##
#  Create a form to get the visitor's name and email address
#  Reference:
#     https://pythonspot.com/flask-web-forms/
#
from flask import Flask, flash, redirect, render_template, request, url_for
from form import NameEmailForm

#  App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route( "/" )
def index():
   return redirect( url_for('contactme') )

@app.route("/contactme", methods=['GET', 'POST'])
def contactme():
   form = NameEmailForm( request.form )

   if request.method == 'POST':
      name = form.name.data
      email = form.email.data
      print( "name: ", name, "email: ", email )

      if form.validate():
         flash( 'Thanks, we will be in touch with you soon, ' + name + '!' )
      else:
         print( "form.errors:", form.errors )
         ## for error_field in form.errors:
         ##    flash( error_field.key, ":", error_field.value )
         flash( form.errors )

   return render_template( 'contactme.html', form=form )

if __name__ == "__main__":
    app.run()
