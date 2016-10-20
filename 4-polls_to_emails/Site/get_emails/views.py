from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import SubscriberEmail

##
# See https://docs.djangoproject.com/en/1.10/intro/tutorial01/#write-your-first-view
#
def index(request):
   subscribedCount = SubscriberEmail.getCountSubscribed()
   unsubscribedCount = SubscriberEmail.getCountUnsubscribed()
   totalCount = SubscriberEmail.getCountAll()

   context = {
      'subscribedCount': subscribedCount,
      'unsubscribedCount': unsubscribedCount,
      'totalCount': totalCount,
   }
   return render( request, 'get_emails/index.html', context )

##
# Super-simple (Un)Subscribe form
#
def subscribe( request ) :
   subscribed = True
   email = 'joe@example.com'
   name = 'Joe'
   site_name = 'groja.com'
   context = {
      'subscribed': subscribed,
      'email': email,
      'name': name,
      'site_name': site_name,
   }
   return render( request, 'get_emails/subscribe.html', context )
## return HttpResponse( 'TODO: build the get_emails subscribe form.' )

