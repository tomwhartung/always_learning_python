#
# Trying the example from Chapter 1 of Lightweight Django O'Reilly e-book
#

import sys
from django.conf import settings

settings.configure(
   DEBUG=True,
   SECRET_KEY='secretkeybitches',
   ROOT_URLCONF=__name__,
   MIDDLEWARE_CLASSES=(
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ),
)

from django.conf.urls import url
from django.http import HttpResponse

def index( request ) :
   return HttpResponse( 'Hello World' )

urlpatterns = (
   url( r'^$', index ),
)

if __name__ == "__main_" :
   from django.core.management import execute_from_command_line
   execute_from_command_line( sys.argv )
