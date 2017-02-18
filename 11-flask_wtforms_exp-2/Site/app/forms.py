##
# Reference:
#   From the first section, "Creating a Form:"
#     https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
#
from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
 
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
