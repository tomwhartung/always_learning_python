##
# Model definitions for the 4-polls_to_emails project
#
from django.db import models
from django.utils import timezone

#
# SubscriberEmail model
#
class SubscriberEmail( models.Model ) :
   GROJA_COM = 'gr'
   SEEOURMINDS_COM = 'sm'
   TOMWHARTUNG_COM = 'tw'
   TOMHARTUNG_COM = 'th'
   SITE_UNKNOWN = 'xx'
   SITE_CODE_CHOICES = (
      ( GROJA_COM, 'groja.com' ),
      ( SEEOURMINDS_COM, 'seeourminds.com' ),
      ( TOMWHARTUNG_COM, 'tomwhartung.com' ),
      ( TOMHARTUNG_COM, 'tomhartung.com' ),
      ( SITE_UNKNOWN, 'site_unknown' ),
   )
   name = models.CharField(
      max_length=45,
      default='',
   )
   email = models.CharField(
      max_length=254,
   )
   site_code = models.CharField(
      max_length=2,
      choices=SITE_CODE_CHOICES,
      default=SITE_UNKNOWN,
   )
   subscription_date = models.DateTimeField(
      'date subscribed',
      default=timezone.now(),
   )

   ##
   # Given a site_code, this method returns the corresponding site name
   #
   def getSiteName( site_code ) :
      ##
      ## for( index=0; index < self.SITE_CODE_CHOICES.length; index++ ) :
      ## site = self.SITE_CODE_CHOICES[self.site_code]
      ##
      for site_pair in SubscriberEmail.SITE_CODE_CHOICES :
         print( site_pair )
         if( site_pair[0] == site_code ) :
            return site_pair[1]

   ##
   # Given a site_code, this method returns the corresponding site name
   #
   def getSiteNameSelfVersion( self, site_code ) :
      ##
      ## for( index=0; index < self.SITE_CODE_CHOICES.length; index++ ) :
      ## site = self.SITE_CODE_CHOICES[self.site_code]
      ##
      for site_pair in SubscriberEmail.SITE_CODE_CHOICES :
         print( site_pair )
         if( site_pair[0] == site_code ) :
            return site_pair[1]

   ##
   # Creates a string representation of the given object
   #
   def __str__( self ) :
      if( self.name == '' ) :
         name = ''
      else :
         name = ' (' + self.name + ')'

      site_name = 'wtf'
      site_code = self.site_code
      ## print( 'self.site_code[0]: "' + self.site_code[0] )
      ## print( 'self.site_code: "' + self.site_code )
      ## print( 'site_code: "' + site_code )
      site_name_1 = SubscriberEmail.getSiteName( site_code )
      site_name_2 = self.getSiteNameSelfVersion( site_code )
      print( 'site_name_1: "' + site_name_1 )
      print( 'site_name_2: "' + site_name_2 )

      subscriberString = self.email + name + ' ' + site_name
      return subscriberString

