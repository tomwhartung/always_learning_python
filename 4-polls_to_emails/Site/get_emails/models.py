##
# Model definitions for the 4-polls_to_emails project
#
from django.db import models

#
# SubscriberEmail model
#
class SubscriberEmail( models.Model ) :
   GROJA_COM = 'gr'
   SEEOURMINDS_COM = 'sm'
   TOMWHARTUNG_COM = 'tw'
   TOMHARTUNG_COM = 'th'
   SITE_UNKNOWN = 'uk'
   SITE_CODE_CHOICES = (
      ( GROJA_COM, 'groja.com' ),
      ( SEEOURMINDS_COM, 'seeourminds.com' ),
      ( TOMWHARTUNG_COM, 'tomwhartung.com' ),
      ( TOMHARTUNG_COM, 'tomhartung.com' ),
      ( SITE_UNKNOWN, 'site_unknown' ),
   )
   name = models.CharField( max_length=45 )
   email = models.CharField( max_length=254 )
   site_code = models.CharField(
      max_length=2,
      choices=SITE_CODE_CHOICES,
      default=SITE_UNKNOWN,
   )
   subscription_date = models.DateTimeField('date subscribed')

   def __str__( self ) :
      subscriberString = self.email + ' (' + self.name + ') ' + self.site_code
      return subscriberString

