from django.shortcuts import render

from django.http import HttpResponse

##
# See https://docs.djangoproject.com/en/1.10/intro/tutorial01/#write-your-first-view
#
def index(request):
   return HttpResponse( 'Hi from the get_emails index.' )

##
# Super-simple (Un)Subscribe form
#
def subscribe( request ) :
   return HttpResponse( 'TODO: build the get_emails subscribe form.' )

