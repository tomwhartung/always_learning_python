##
# views.py: view functions for our get_emails app
#
from django.shortcuts import get_object_or_404
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
def subscribe( request, id ) :
   if( id == '0' ) :
      subscribed = False
      email = 'you@email.com'
      name = ''
      site_name = 'groja.com'
   else :
   ## subscriberEmail = SubscriberEmail.objects.get( pk=id )
      subscriberEmail = get_object_or_404( SubscriberEmail, pk=id )
      subscribed = subscriberEmail.subscribed
      email = subscriberEmail.email
      name = subscriberEmail.name
      site_code = subscriberEmail
      site_name = SubscriberEmail.getSiteName( site_code )
   context = {
      'id': id,
      'subscribed': subscribed,
      'email': email,
      'name': name,
      'site_name': site_name,
   }
   return render( request, 'get_emails/subscribe.html', context )
## return HttpResponse( 'TODO: build the get_emails subscribe form.' )

