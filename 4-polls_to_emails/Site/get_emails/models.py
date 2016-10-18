##
# Model definitions for the 4-polls_to_emails project
#
from django.db import models

#
# SubscriberEmail model
#
class SubscriberEmail( models.Model ) :
   name = models.CharField( max_length=45 )
   email = models.CharField( max_length=254 )
   site_code = models.CharField( max_length=2 )
   subscription_date = models.DateTimeField('date subscribed')

   def __str__( self ) :
      subscriberString = self.email + ' (' + self.name + ')' + self.site_code
      return self.email

