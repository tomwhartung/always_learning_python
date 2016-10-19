from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import SubscriberEmail

##
# See https://docs.djangoproject.com/en/1.10/intro/tutorial01/#write-your-first-view
#
def index(request):
   ####
   #### First try, but it could be considered "doing modelly things in the view:"
   ####
   ## subscribedCount = SubscriberEmail.objects.filter(subscribed=True).count()
   ## unsubscribedCount = SubscriberEmail.objects.filter(subscribed=False).count()
   ## totalCount = SubscriberEmail.objects.all().count()
   ##
   ## Second try: a better way, I think, "more pure:"
   ##
   subscribedCount = SubscriberEmail.getCountSubscribed()
   unsubscribedCount = SubscriberEmail.getCountUnsubscribed()
   totalCount = SubscriberEmail.getCountAll()

   template = loader.get_template('get_emails/index.html')
   context = {
      'subscribedCount': subscribedCount,
      'unsubscribedCount': unsubscribedCount,
      'totalCount': totalCount,
   }
   return HttpResponse( template.render(context,request) )

##
# Super-simple (Un)Subscribe form
#
def subscribe( request ) :
   return HttpResponse( 'TODO: build the get_emails subscribe form.' )

