##
#  Functions used by this app to send emails
#  References:
#     Chapter 6 of Flask Web Development by Miguel Grinberg
#
from flask_mail import Mail
from flask_mail import Message

##
#  First: send a simple test email
#
def send_test_email( message ):
   print( 'In send_test_email(), message =', message )
   return True
