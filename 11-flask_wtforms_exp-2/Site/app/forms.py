##
# Reference:
#   From the first section, "Creating a Form:"
#     https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
#   Added updates from the second part of the tutorial:
#     https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
#
from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
  ## name = TextField( "Name",  [validators.Required("Please enter your name.")] )
  name = TextField( "Name" )
  email = TextField( "Email",
    [ validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address") ] )
  subject = TextField("Subject",  [validators.Required("Please enter a subject line.")])
  message = TextAreaField( "Message",  [validators.Required("Please enter a message.")] )
  submit = SubmitField( "Send" )
