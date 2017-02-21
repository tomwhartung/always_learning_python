##
#  Create a form to get the visitor's name and email address
#  Reference:
#     https://pythonspot.com/flask-web-forms/
#
from flask import Flask, render_template, flash, request
from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email

#  App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class NameEmailForm( Form ):
   name = StringField( 'Name:' )
   email = StringField( 'Email:',
      [Required("Please share your email address so that we can contact you."),
       Email("Please enter a valid email address.")] )
   submit = SubmitField( 'Get Your Portrait' )

   def reset(self):
      blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
      self.process(blankData)


@app.route("/", methods=['GET', 'POST'])
def hello():
   form = NameEmailForm( request.form )

   print( "form.errors:", form.errors )
   if request.method == 'POST':
      name = request.form['name']
      email = request.form['email']
      print( "name: ", name, "email: ", email )

      if form.validate():
         flash( 'Thanks, we will be in touch with you soon, ' + name + '!' )
      else:
         flash( 'Error: All the form fields are required.' )

   return render_template( 'hello.html', form=form )

if __name__ == "__main__":
    app.run()
