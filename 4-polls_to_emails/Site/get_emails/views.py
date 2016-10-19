from django.shortcuts import render

from django.http import HttpResponse
from .models import SubscriberEmail

##
# See https://docs.djangoproject.com/en/1.10/intro/tutorial01/#write-your-first-view
#
def index(request):
   ##
   ## First try, but it could be considered "doing modelly things in the view:"
   ##
   ## subscribedCount = SubscriberEmail.objects.filter(subscribed=True).count()
   ## unsubscribedCount = SubscriberEmail.objects.filter(subscribed=False).count()
   ## totalCount = SubscriberEmail.objects.all().count()
   #
   # A better way, I think, "more pure:"
   #
   subscribedCount = SubscriberEmail.getCountSubscribed()
   unsubscribedCount = SubscriberEmail.getCountUnsubscribed()
   totalCount = SubscriberEmail.getCountAll()
   response = 'Hi from the get_emails index.  '
   response += 'Number of subscribed emails: ' + str( subscribedCount ) + '. '
   response += 'Number of unsubscribed emails: ' + str( unsubscribedCount ) + '. '
   response += 'Total of all emails: ' + str( totalCount ) + '. '
   return HttpResponse( response )

##
# Super-simple (Un)Subscribe form
#
def subscribe( request ) :
   return HttpResponse( 'TODO: build the get_emails subscribe form.' )

