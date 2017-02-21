##
#  Create a form to get the visitor's name and email address
#  Reference:
#     https://pythonspot.com/flask-web-forms/
#
from flask import Flask, render_template, flash, request
from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Optional, Required, Email

#  App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class NameEmailForm( Form ):
   name = StringField( 'Name:', validators=[Optional()] )
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

   return render_template( 'hello.html', form=form )

if __name__ == "__main__":
    app.run()
