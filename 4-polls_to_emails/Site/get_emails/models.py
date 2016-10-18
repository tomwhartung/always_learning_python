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

   ##############################
   # Two versions of getSiteName
   # ---------------------------
   # Given a site_code, these methods return the corresponding site name
   # I am keeping both versions around until I decide which one I think is better
   #
   ###
   ### TODO:
   ###   There should be a way to look up the value instead of using a for loop
   ### Something like:
   ###   for( index=0; index < self.SITE_CODE_CHOICES.length; index++ ) :
   ###   site = self.SITE_CODE_CHOICES[self.site_code]
   ###
   ##
   # Note that this version has only one argument, and we call it like this:
   #   SubscriberEmail.getSiteName( site_code )
   #
   def getSiteNameSingleArg( site_code ) :
      for site_pair in SubscriberEmail.SITE_CODE_CHOICES :   # Note the use of "SubscriberEmail."
         if( site_pair[0] == site_code ) :
            return site_pair[1]

   ##
   # Note that this version has two arguments, and we call it like this:
   #   self.getSiteNameSelfVersion( site_code )
   #
   def getSiteNameSelfVersion( self, site_code ) :
      for site_pair in self.SITE_CODE_CHOICES :     # Note the use of "self."
         if( site_pair[0] == site_code ) :
            return site_pair[1]
   ##############################

   ##
   # Creates a string representation of the given object
   #
   def __str__( self ) :
      id = '\n\t#' + str( self.id )
      email = ': ' + self.email

      if( self.name == '' ) :
         name = ''
      else :
         name = ' (' + self.name + ')'

      site_code = self.site_code
      site_name = ' ' + SubscriberEmail.getSiteNameSingleArg( site_code )
      ## site_name = ' ' + self.getSiteNameSelfVersion( site_code )

      subscription_date = ' ' + str( self.subscription_date ) + '\n'

      subscriberString = id + email + name + site_name + subscription_date
      return subscriberString

